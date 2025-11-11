---
title: TPM2-backed SSH keys on NixOS
summary: How to set up and use a hardware-backed SSH key tied to your system in a NixOS environment.
posted_on: 2022-08-18
---

## Introduction

If you are here, I am assuming you already know why it's useful to store keys on a TPM, so I won't write about my rationale here.

There are a few components to understand here:

* The TPM hardware itself generates and stores keys
* `tpm2-abrmd` is the Access Broker and Resource Manager Daemon, which exposes access to the TPM chip over dbus
* `tpm2-pkcs11` provides a PKCS#11 interface to keys stored on the TPM, allowing many applications (including OpenSSH) a way to use the keys managed by the TPM

## Installation

Let's make sure those components are all installed and configured appropriately:

* You may need to enable the TPM in your system's firmware setup. Be sure to enable it as in 2.0 mode; certain ThinkPads seem to support 1.2 and 2.0 but only 2.0 will work for this.
* Install all of the components required. On NixOS, that's this snippet in your `configuration.nix`:

```nix
security.tpm2 = {
  enable = true;
  pkcs11.enable = true;
  abrmd.enable = true;
};

environment.systemPackages = [
  # your other desired systemPackages
  tpm2-tools
];
```

* The next steps will need to be completed as your regular user. You will need the environment variable `TPM2TOOLS_TCTI` set to `tabrmd:bus_type=system`. I use `home-manager`, so I configured this in `home.sessionVariables`, but you can add an `export` in your shell initialization file and it should work fine that way too. To cause less noise later on, set `TSS2_LOG` to `fapi+NONE` too.

## Configuring the TPM

Now we can initialize the TPM and generate our keys.

First, initialize an object hierarchy within the TPM, store that information in `tpm2-pkcs11`'s database, and return a handle that we can use in future commands.

```
% tpm2_ptool init
action: Created
id: 1
```

The `id` returned is that of the "primary object" of the hierarchy. We will need this number in future commands. It's probably `1`, but change the `--pid` option in later commands if you need to.

Next, we'll create a PKCS11 token. You have to pass a sopin ("system operator" PIN, for recovery/admin purposes) and a userpin (the PIN you will usually use to unlock the keys of this token) on the command line in this step, so consider `export HISTFILE=/dev/null` so those don't get stored in your shell history.

The `label` can be anything you want, and both PINs can contain non-numeric characters if you like.

```console
$ tpm2_ptool addtoken --pid=1 --label=ftpmtoken1 --sopin=youradminpassword --userpin=youruserpassword
```

Next, create a key on the newly created token. `--label` and `--userpin` must match what you used before. Multiple algorithms are available (`tpm2_ptool addkey --help`) but not all of them are necessarily supported by your TPM.

To see if your TPM supports a specific ECC curve, try `tpm2_getcap ecc-curves`. To see if your TPM supports a specific RSA key size, try `tpm2_testparms rsa[bits]`, like `tpm2_testparams rsa4096`. If no error is returned, you can use that key size.

```console
$ tpm2_ptool addkey --algorithm=ecc256 --label=ftpmtoken1 --userpin=youruserpassword
```

## Configuring OpenSSH

Now we can get our public key from the TPM:

```console
$ ssh-keygen -D /run/current-system/sw/lib/libtpm2_pkcs11.so
WARNING: Listing FAPI token objects failed: "fapi:A parameter has a bad value"
Please see https://github.com/tpm2-software/tpm2-pkcs11/blob/master/docs/FAPI.md for more details
WARNING: FAPI backend was not initialized.
ecdsa-sha2-nistp256 [...]
```

You can safely ignore the FAPI warnings, if any appear for you. Install the SSH public key on whatever hosts you need to access, then:

```console
$ ssh -o IdentityAgent=none -o PKCS11Provider=/run/current-system/sw/lib/libtpm2_pkcs11.so user@host
```

You should be prompted for your token PIN here.

You only need to set `IdentityAgent=none` to bypass using your usual SSH agent (in my case, this is `gpg-agent` configured to use keys stored on a YubiKey, so I'm skipping the "insert token" prompt this way).

You may configure these options in your `~/.ssh/config` as well, to save on typing.

## Potential future work

* Get keys stored with the Feature API instead of just ignoring errors (this is the `fapi` in `TSS2_LOG=fapi+NONE`)
* Ignore errors even harder (I already do this [here](https://github.com/an-empty-string/home-config/blob/main/sys/modules/laptop.nix#L112), I just haven't documented it yet)
* Bind keys to boot measurements
* Use keys in other applications (like Firefox for HTTPS client certs)

## References

- [leo60228.space](https://leo60228.space/trusting-ssh-keys-using-a-centralized-hardware-secret/), some of the `tpm2-pkcs11` commands originally came from here!
