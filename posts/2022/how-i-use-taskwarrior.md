---
title: How I use Taskwarrior
summary: Notes on my todo list workflow using Taskwarrior; future work.
posted_on: 2022-08-25
---

[Taskwarrior](https://taskwarrior.org/) is a neat command-line task tracking tool; this page describes how I use the tool, with explanations of [my configuration](https://github.com/an-empty-string/home-config/blob/main/home/productivityTools.nix).

## The basics

* I override the `priority` user-defined attribute to provide more values than the 3 defaults (H, M, L for High, Medium, Low respectively). I added N (for "Now") and S (for "Someday" or "Soon(TM)") at the highest and lowest ends of the scale.
* My [primary report](https://github.com/an-empty-string/home-config/blob/main/home/productivityTools.nix#L8) totally ignores the built-in urgency calculation, instead grouping tasks by project and priority. I find this easier to deal with: since I'm not very good at regularly reviewing tasks, this keeps everything in front of me and encourages me to work on things that are interesting to me right now (instead of forcing myself to focus on something that the urgency calculation thinks is good).
* [I use contexts](https://github.com/an-empty-string/home-config/blob/main/home/productivityTools.nix#L37) when I need to focus on one particular project. For example, I have contexts for personal work, my full-time job, and various contracted projects I work on.
* I use Taskwarrior to keep track of [books I'm reading](https://github.com/an-empty-string/home-config/blob/main/home/productivityTools.nix#L16) but exclude these from my main reports.
* I use a [custom next report](https://github.com/an-empty-string/home-config/blob/main/home/productivityTools.nix#L24) when I really do need the computer to pick something for me to do. The beauty of my `next` command is that it will only display a single highest-priority work item. If I don't like it, it's an indication that I'm working in the wrong context or need to reorganize my tasks. The `next` command respects the "+today" tag and only gives me tasks that I've indicated I want to finish today.
* I use a UDA called "size" to try to predict how many items I can complete per day. Generally, in an 8-hour workday, I can accomplish 4-5 Small tasks, 2-3 Medium tasks, or 1 Large task. If a task will take longer than a workday, it probably should be broken down further.

## Syncing

* I use a [taskserver](https://github.com/an-empty-string/home-config/blob/main/sys/trisfyi/configuration.nix#L259) to synchronize tasks across all my computers.
* I synchronize my tasks [every ten minutes](https://github.com/an-empty-string/home-config/blob/main/home/productivityTools.nix#L71) automatically.

## Periodics

I define [periodic scripts](https://github.com/an-empty-string/home-config/blob/main/home/productivityToolsPeriodic.nix) which are supposed to automatically manage tags (e.g. retagging "+tomorrow" tasks to "+today") for me. This does not really work and I haven't had time to troubleshoot yet.

I also use periodics to build out a [scheduled push notification tool](https://github.com/an-empty-string/home-config/blob/main/home/productivityToolsPeriodic.nix#L30).

## Future improvements

I need to build out a better **inboxing** system. Right now, I add tasks to Taskwarrior when I remember to do so. I'd like a way to add tasks to a special "inbox" queue from any device (through a Tasker task, simple shell alias, whatever) and be nagged about them until I classify/prioritize them.

I need to get better at periodically reviewing tasks, making sure priorities are up to date, etc.

I need to fix the periodics system so it actually works.
