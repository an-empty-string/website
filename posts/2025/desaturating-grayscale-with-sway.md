---
title: Desaturating the desktop (grayscale mode) with Sway
posted_on: 2025-03-23
show_toc: false
---

Like [a few other folks](https://www.reddit.com/r/swaywm/comments/ffc7mv/setting_sway_grayscale_monochromatic/), I use the computer much more easily when there are not bright colors involved. Some Wayland desktop environments, like GNOME, support [extensions to do this](https://askubuntu.com/a/1013262). This is great, but I have a strong preference for using a tiling window manager for a number of reasons.

My tiling window manager of choice, [Sway](https://swaywm.org/), does not have support for a grayscale mode, or saturation controls of any kind. So I hacked them on.

## How?

I added patches to [wlroots' GLES fragment shaders](https://github.com/an-empty-string/wlroots-hacks/commit/5e1fd11c3938058ceb6bf224d9991539a49f14c2#diff-92092e81d230e67c820b4e2b60ba7d0bdb78e4dad117076ec97edd5dd4a4c629) to add desaturation support just before drawing to the screen, [disabled the Vulkan renderer](https://github.com/an-empty-string/wlroots-hacks/blob/tris-patches/flake.nix#L12), [plumbed this into Sway](https://github.com/an-empty-string/sway-hacks/commit/5fb240efadf85387eb35998bf1895e25987cd1fb), and [wrapped it all up in a Nix flake](https://github.com/an-empty-string/sway-hacks/blob/tris-patches/flake.nix).

Thanks to [Izzy](https://izzy.horse) for helping me understand the graphics concepts involved here.

This is not good code and it won't be upstreamed in this form. But it solves an accessibility need for me, so that's okay. If you are okay with all of this, you can either build my [sway](https://github.com/an-empty-string/sway-hacks) and [wlroots](https://github.com/an-empty-string/wlroots-hacks) "forks" yourself, or use them in a home-manager configuration with something like this:

In `flake.nix`:

```nix
inputs.sway-tris = {
  url = "github:an-empty-string/sway-hacks/tris-patches";
  inputs.nixpkgs.follows = "nixpkgs";
}

outputs = { ..., sway-tris, ... }: {
  homeConfigurations = let
    extraSpecialArgs.sway-tris = sway-tris.packages.x86_64-linux.default;
  in {
    inherit extraSpecialArgs;
    modules = [ home.nix ];
  }
}
```

In `home.nix` or your equivalent:

```nix
{ ..., sway-tris, ... }: {
  wayland.windowManager.sway.package = sway-tris;
}
```

Then, in your Sway config, make keybinds like:

```
bindsym Mod4+Shift+d set $grayscale 0.75
bindsym Mod4+Shift+f set $grayscale 0
bindsym Mod4+Shift+g set $grayscale 1
```

This config would make Shift+Super+f disable desaturation, Shift+Super+g enable complete desaturation, and Shift+Super+d enable partial desaturation. Note that the scaling factor isn't perceptually linear (like 20% desaturation doesn't mean your eyes will perceive 80% of the color &mdash; in fact `set $grayscale 0.2` was pretty much imperceptible when I was testing).


## The "right" way...

...is probably to hook into the Vulkan renderer's color transform infrastructure, like [ICC profile-based color calibration support](https://gitlab.freedesktop.org/wlroots/wlroots/-/blob/master/render/color_lcms2.c?ref_type=heads) does, and write a new color transform type that applies either a desaturation transformation, or a more generic transformation (like being able to specify a matrix to multiply the drawn colors by; that could support other color accessibility needs too). Then you could hook into [Sway's output color profile support](https://github.com/swaywm/sway/blob/master/sway/commands/output/color_profile.c).

I haven't done this yet, but would like to, because it has a much better chance of landing upstream :)
