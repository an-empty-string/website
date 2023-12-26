---
title: Creating a test CA using the Smallstep CLI
summary: How to quickly bypass the usual safety checks when using the Smallstep CLI to get a CA up and running quickly.
posted_on: 2021-11-19
show_toc: no
---

The `step` command-line tool has lots of guardrails to prevent you from creating a certificate authority in an insecure manner; these are very inconvenient when you just want a few certificates to play around with. Here is my usual test script which bypasses all of this:

```
step certificate create ca ca.crt ca.key --profile root-ca --no-password --insecure
step certificate create one one.csr one.key --csr --profile leaf --no-password --insecure
step certificate create two two.csr two.key --csr --profile leaf --no-password --insecure
step certificate sign one.csr ca.crt ca.key > one.crt
```
