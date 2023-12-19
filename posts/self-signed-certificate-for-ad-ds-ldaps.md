---
title: Self-signed certificate for AD DS LDAPS
posted_on: 2020-10-14
show_toc: no
---

Sometimes you need to talk to Active Directory Domain Services using a secure LDAP connection but you're okay with using a self-signed certificate (in my case, I have a set of internal tools which can be told not to validate certificates, but enforces TLS; I use these internal tools before deploying Certificate Services and a trusted certificate). Here is how to do it.

You need to run all of these commands in an elevated PowerShell prompt.

```powershell
$name = "dc.ad.companydomain.com"
$cert = New-SelfSignedCertificate -DnsName $name -CertStoreLocation Cert:\LocalMachine\My

$path = "HKLM:\Software\Microsoft\Cryptography\Services\NTDS\SystemCertificates\My\Certificates"
if(!(Test-Path $path)) { New-Item -Force $path }

Copy-Item -Path "HKLM:\Software\Microsoft\SystemCertificates\My\Certificates\$($cert.Thumbprint)" -Destination $path
```

The certificate will immediately start being used by AD DS; you don't need to restart services or reboot the machine. AD DS uses the standard LDAPS port (636).
