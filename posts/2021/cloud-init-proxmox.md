---
title: Debian, cloud-init, and Proxmox
summary: Notes on making the Debian cloud images work in Proxmox.
posted_on: 2021-04-15
show_toc: no
---

The Debian OpenStack cloud images will work fine in Proxmox if you add a serial port to the VM (if you don't have a serial port, they won't boot properly).

If you specify the username `root` in your cloud-init configuration, cloud-init will ignore SSH key options (like the "cert-authority" flag). Specify any other username and your SSH key options will be respected.
