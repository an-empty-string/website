---
title: Polycom provisioning notes
summary: Notes on the XML format used to provision Polycom phones.
posted_on: 2021-06-21
show_toc: no
---

Phones look at all attributes on any XML element in the provisioning file and collect them together to build their configuration. So these are equivalent:

* `<set foo="bar" foo.baz="quux" />`
* `<foo foo="bar"><baz foo.baz="quux" /><xyzzy /></foo>`

Anything in the `device` namespace will not be applied unless you have a `device.set="1"` and a `device.some.attr.set="1"` for each `device.some.attr` you want to set. Setting many device attributes (especially those related to provisioning) may cause the phone to reprovision. This is probably what you want.

When running HTTP provisioning, phones may `PUT` files to you. Usually, these files are prefixed with `/phonemac-`. If you can authenticate phones, you can thus authenticate file uploads pretty easily.

Note that phone passwords must not be longer than 32 characters. If you try to do this, the provisioning password will not be saved to flash and you will see the error `cfgFlashUpdate: Length [n] is longer than 32 for device.prov.password` in the phone's app log.
