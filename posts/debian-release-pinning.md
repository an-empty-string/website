---
title: Pinning Debian packages to stable
summary: Notes on using apt pinning to mix Debian packages from different distribution releases.
posted_on: 2020-10-17
show_toc: no
---

While it's not advisable to have packages from multiple Debian release versions on your system at the same time, it is possible, and using release pinning can make this work mostly correctly.

Here's what I use to accomplish this in `/etc/apt/preferences.d/pin-testing.pref`:

```
Package: *
Pin: release a=stable
Pin-Priority: 1000

Package: *
Pin: release a=testing
Pin-Priority: 500
```

The generic format of a pin entry is

```
Package: name
Pin: (origin|version|release) ...
Pin-Priority: number
```

Release pins can be for `v=10` (version number), `n=bullseye` (codename), or `a=stable` (archive name).

The `apt_preferences(5)` manual page has more info.
