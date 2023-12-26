---
title: My Pomodoro tool
summary: How to install and use my MQTT-based Pomodoro system.
posted_on: 2021-04-09
show_toc: no
---

Back in February I wrote a [Pomodoro tool](https://gist.github.com/an-empty-string/a4706537cd9ffaf5f67d3f49a8540fea) which runs as a service on your own machine and communicates using MQTT. Here is how to use it:

* Make sure you have a newish Python (probably 3.7 or higher? not sure) and MQTT daemon running locally (I use mosquitto)
* Install the script's Python dependency: `pip install asyncio-mqtt`
* Write a JSON config object to `~/.pomodoro.json` including the keys `work_time` and `break_time`: `{"work_time": 1500, "break_time": 300}` is a standard Pomodoro timer. You can also set `wait_for_break` to true to require sending the trigger command to start a break after a work period (the default) or false to automatically continue to a break. You can also set `use_emoji` to true to use emoji (I don't remember what this means)
* Download the script and put it somewhere (I use my `~/bin` for this)
* Set it up to run on login using a systemd unit or something and start the script
* Get statusline output with `mosquitto_sub -t pomodoro/statusline`
* Send commands to the service with `mosquitto_pub -t pomodoro/command -m action`. The action can be `trigger` (start/pause timer), `reset` (resets timer), `done` (stops the current work period and moves to a break), and `reload` (reloads config).

I use this systemd unit in `~/.config/systemd/user/pomodoro.service` (`systemctl --user enable --now pomodoro.service`):

```ini
[Unit]
Description=Pomodoro daemon service

[Service]
ExecStart=/home/tris/.pyenv/shims/python3 %h/bin/pomodoro.py

[Install]
WantedBy=default.target
```

I use this config in my `~/.i3blocks.conf` to display timer status:

```ini
[pomodoro]
label=🍅
command=mosquitto_sub -t pomodoro/statusline
interval=persist
```

I use these shell aliases also:

```sh
alias pom='mosquitto_pub -t pomodoro/command -m'
alias pt='pom trigger'
```

You can subscribe to the topics `pomodoro/state` and `pomodoro/time-remaining` from your own tools if you want to do stuff like send a notification whenever you should take a break.
