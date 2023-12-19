---
title: How to change PowerShell remoting permissions
posted_on: 2020-10-23
show_toc: no
---

```powershell
Set-PSSessionConfiguration -Name Microsoft.PowerShell -showSecurityDescriptorUI
```

This command will bring up a permissions GUI which lets you change who can create WinRM sessions on the computer you run it on.
