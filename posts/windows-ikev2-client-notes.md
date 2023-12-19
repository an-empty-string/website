---
title: Windows IKEv2 client notes
posted_on: 2020-12-04
show_toc: no
---

Here are some things I found unintuitive about the built-in Windows IKEv2 VPN client:

* Parent SAs and child SAs need not use the same algorithms.
* To use 256-bit AES, set `HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services\Rasman\Parameters\NegotiateDH2048_AES256` to the DWORD value 1.
* If using a non-Windows/RRAS server, set IKE lifetime (not necessarily SA lifetime) to ~30 minutes or so. Windows' SA lifetime is about an hour, but if it initiates a parent SA rekey on its own, things won't work right. Let the responder initiate a SA rekey.
* If possible/allowed, just don't specify DH groups. I don't like this but it seems like e.g. Libreswan remains FIPS 140-2 validated when run without DH groups specified. I used the aes256-sha1 cipher suite for both `ike=` and `phase2alg=`.
