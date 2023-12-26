---
title: MikroTik point-to-point link packet loss and latency spikes
summary: "Why your 802.11 point-to-point link with a MikroTik device as client breaks periodically and how to fix it."
posted_on: 2021-01-19
show_toc: no
---

At home, I run a pair of SXTsq 5 ac devices to span my network to a place where
I can't be bothered to run a cable to just yet. After installing a VoIP phone
in that location, I noticed reoccurring periods of time (about 17 seconds each,
maybe varying from 15-20 seconds) where packet loss was high. This was made
clear by choppy audio on phone calls.

After further debugging, these drops were occurring almost 5 minutes apart,
down to the second. I initially thought this was some external interference
source, but that was not the case (confirmed with another device and the
frequency-monitor tool built-in to RouterOS). It turns out that RouterOS
wireless clients will automatically scan for APs with better signal when they
are connected to an 802.11 wireless network. This process can cause
disconnections and periods of high latency.

You can disable this behavior with `/interface wireless set station-roaming=disabled [interface].`
