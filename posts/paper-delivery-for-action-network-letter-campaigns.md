---
title: How to deliver letters on paper for an Action Network letter campaign
summary: Getting your supporters to send emails to legislators is great, but dropping paper on their desks can be even better! Here is a tool to help you do that.
posted_on: 2025-03-04
show_toc: false
---

At [ALTRAC](https://altrac.works) we run a lot of letter campaigns on [Action Network](https://actionnetwork.org). These let us write template letters that our supporters can send to their state legislators really easily &mdash; they enter their address, optionally add their own stories to our template letter (or rewrite it entirely), and Action Network does the rest (geocodes them to their districts, remembers those districts for next time, and sends emails to their legislators).

This is great, but we know plenty of legislators just do not read their email at all, so we wanted to hand-deliver constituent letters to their desks too. Action Network provides the data we need for this on [the "target report"](https://help.actionnetwork.org/hc/en-us/articles/203846445-Downloading-the-target-report), but that's a .csv &mdash; we need to turn it into something printable.

I've written a tool to do this! Go to [https://tris.fyi/print-letter-delivery/](https://tris.fyi/print-letter-delivery/), upload a target report from Action Network, hit Ctrl-P, tweak print options in your browser, print, and you're done! tris.fyi never sees your data &mdash; the reformatting is done entirely in your web browser. [!If you're interested in technical details, just hit "View Source"! I haven't obfuscated or minified the JavaScript involved so it should be pretty easy to follow.!] In case you don't want to print letters for certain targets (e.g. you use [custom targets](https://help.actionnetwork.org/hc/en-us/articles/203112879-Uploading-custom-targets-for-call-campaigns-and-letter-campaigns) to contact committees in bulk) you'll see a target filter after uploading your report; uncheck targets to exclude them from the print copy.

While Action Network is my employer, this tool was written in my personal capacity, so please don't go telling our support folks about issues! Email me instead (tris@tris.fyi) and I will help you out :)
