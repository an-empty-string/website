---
title: Using an ELM327 OBD-II interface on NixOS
posted_on: 2024-02-10
show_toc: no
---

In `configuration.nix` or equivalent, enable legacy compatibility mode in `bluetoothd`:

```nix
systemd.services.bluetooth.serviceConfig.ExecStart = lib.mkForce [
  ""
  "${config.hardware.bluetooth.package}/libexec/bluetooth/bluetoothd -f /etc/bluetooth/main.conf -C"
];
```

It is probably best to reboot your machine after this. Next, pair and trust your ELM327 device:

```
tris@dripleaf ~ % bluetoothctl
[bluetooth]# scan on
Discovery started
[NEW] Device AA:BB:CC:11:22:33 OBD-II

[bluetooth]# pair AA:BB:CC:11:22:33
(... you may have to enter a PIN specific to your device, maybe try 1234 ...)

[bluetooth]# trust AA:BB:CC:11:22:33
Changing AA:BB:CC:11:22:33 trust succeeded
```

Next, discover the serial channel:

```
tris@dripleaf ~ % sdptool browse --l2cap AA:BB:CC:11:22:33
Browsing AA:BB:CC:11:22:33 ...
Service Name: JL_SPP
Service RecHandle: 0x10004
Service Class ID List:
  "Serial Port" (0x1101)
Protocol Descriptor List:
  "L2CAP" (0x0100)
  "RFCOMM" (0x0003)
    Channel: 2
Profile Descriptor List:
  "Serial Port" (0x1101)
    Version: 0x0102
```

The number in the RFCOMM Channel output will be needed in the next step; in my case it was channel 2.

Next, bind an `rfcomm` device node with `rfcomm bind 1 AA:BB:CC:11:22:33 2`. The `1` is the `rfcomm` device number (i.e. in this case we'll end up with `/dev/rfcomm1`) and the `2` is the channel number from the previous step.

Now you can connect to the serial port with a tool like [python-obd](https://python-obd.readthedocs.io/en/latest/) by specifying the rfcomm device you created in the last step.

Good luck!
