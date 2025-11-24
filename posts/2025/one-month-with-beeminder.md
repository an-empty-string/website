---
title: One month with Beeminder
posted_on: 2025-11-24
show_toc: false
---

Other folks with executive function issues are perhaps familiar with the productivity system "novelty problem" --- you finally adopt a new tool, you do a brain dump into it, it feels great, and your life feels like it's on track for a few weeks. Then things start to stagnate: maybe your backlog becomes overwhelming, the system stops tracking reality, and you eventually stop trusting the system's ability to work for you.

And you feel a little bad about it, but not that bad, because you still feel like you're still (sometimes just barely) skating by, so maybe you didn't even need the system anyway...? But when you reflect on how you're doing, you know in your heart that you'd be so much better off if you could actually stick to it. [![Intend](https://intend.do/) is an interesting take on an actual solution to this problem, and it integrates with Beeminder! I'm playing with it and might write about it in a future post.!]

I've run into this problem with Google Keep, [Taskwarrior](https://taskwarrior.org/), and [Todoist](https://todoist.com), at least. They're all great tools, and I still consult them to some extent (because I have past todos, or use them to jot down quick reminders, etc), but they will never be able to push me into action.

## The real problem

This post isn't really about productivity systems, though. I have a variant of this problem whenever I try to do _anything_ good for myself that demands long-term effort. [Habitica](https://habitica.com) worked to build a morning routine and help me read more books for a while, but I eventually lost the habit, and just stopped checking the app. [Loop Habits](https://loophabits.org/) felt lower-stress (just a tracking and reminders tool, instead of a game with a little guy you have to keep healthy), and helped me spend more time outside for a few weeks, but eventually fell victim to the same fate. This type of tool just does not motivate me.

There's a deeper problem caused by this type of cycle that I didn't really notice (until I stumbled into starting to solve it). The problem is that *I lose trust in my own ability to follow through on goals* every time I stopped consistently using a system.

From one angle, this is really, really bad! I was very slowly spiraling out of control, making my personal goal-setting loop less effective every time I did it, without even noticing it.

## Working towards a solution

On a sleepless night last month, I came across Daniel Reeves' [Homo Economicus Wannabees](https://www.youtube.com/watch?v=JP7o4uyJalM) talk, about how his family uses markets to resolve friendly disagreements. While I am guessing Daniel's family is unique here and I'd never ever want to adopt these techniques (it takes a certain type of nerd (affectionate) mindset and strong relationships to make this work), it's a fascinating watch.

Then I started clicking around and ended up at [Beeminder](https://www.beeminder.com/) (where Daniel is a co-founder). Beeminder is a graph-based goal-tracking tool --- if you can describe your goal as a line [!an arbitrary piecewise linear function, really, so you can slow down, sprint, or take a complete break!], and your day-by-day progress as points, Beeminder will monitor your progress and let you know when you're falling off track. It'll even pull datapoints automatically from third-party services, like [The StoryGraph](https://thestorygraph.com/) to track your reading, and [Sleep as Android](https://sleep.urbandroid.org/en/) to track your sleep.

The astute reader will notice that a tool providing this set of features alone has the same exact problem as the systems I mentioned above --- there's no push. [!I felt a little weird about writing this post only a month in for exactly this reason! But after reflecting on it, Beeminder feels so dramatically different, and I feel like these insights might be immediately useful for some folks in my circles, that I decided to write it anyway. Look for an update at 6 and 12 months, perhaps!!]

The thing that makes this all work: *if your datapoints end up on the wrong side of the line [!a "derailment", in Beeminder parlance!] (e.g. you didn't do enough one day to meet your goal), Beeminder charges you money*, escalating each time you go off track. In other words, Beeminder is a [commitment device](https://en.wikipedia.org/wiki/Commitment_device) for quantifiable goals.

If your response to that is "wait, what? that's nuts!", well, me too! My initial thoughts went something like:

* That level of committment to my own goals is way too scary for me; I'd collapse under the pressure.
* My goals are too hard to quantify, or are tasks or habits that don't make sense to describe as long-term goals done over time, so this data model won't work for me.
* Surely I'd just cheat if I got too close to falling off-track...?

For me, none of these ended up actually being problems. But I absolutely think Beeminder can be less useful, or outright actively harmful, to some folks in some circumstances; please read through the whole post if you think that might be you. But first...

## What I've accomplished

So much. More than I thought was possible in one month. Specifically:

**I'm reading more consistently.** I started tracking how much I read, and set [a modest goal](https://beeminder.com/tris/readmore-old) of 60 (ereader) pages per day. (I moved to a [StoryGraph-based goal](https://www.beeminder.com/tris/readmore) last week though.)

**I'm actually keeping my apartment tidy.** I used to have problems keeping up with clutter in my living space, but after setting [a goal](https://beeminder.com/tris/livingspace) to average 30 minutes a day working against entropy, this seems mostly solved. This is just a little more than I need to stay on top of dishes/putting things in their proper places, so it forces me to sweep/mop/build furniture that's still in boxes [!I just moved! I swear I don't usually keep furniture in boxes for that long!] too. The amount of time I target will need some tuning, but the principle seems to work great for me.

**I'm back in my journaling habit.** I set [a goal](https://www.beeminder.com/tris/journal) where I enter a "1" every day I make a journal entry. The goal is set for "0.9 journal entries/day", so if I miss a day it doesn't immediately hurt, but I get pulled back into the habit very quickly if I drop off. Working great so far! And This is a counterexample to "my goals are habits that don't make sense to describe as long-term goals done over time" --- "days per day" type metrics work totally fine in Beeminder, though they take a bit to get used to.

**I'm getting out of bed on time.** I set [a goal](https://www.beeminder.com/tris/2025awake) where I enter a "1" every day I actually get out of bed on time. It was hard for me to get external motivation for this before: I work remote with a flexible schedule, so there were no immediate consequences to checking Slack for any critical issues, sleeping in a bit, and working for a little longer than normal. Long-term, it's healthier for me to consistently work set hours (there are occasionally days with exceptions!), and now I can actually reliably do that. The goal is on break for some travel, but I'll likely pull it back to "<nobr>⅞ days</nobr> per day" [!awesome units, right?!] once I'm back, to help keep my weekends consistent too while acknowledging that I have to sleep in sometimes.

This has led to me developing a morning routine, so I have something to look forward to *after* getting out of bed, which is starting to turn this into a self-reinforcing habit.

**I'm able to make consistent forward progress on work that usually feels like a slog.** I have a big batch of work at the end of every year; there are some pieces that I really don't look forward to. That work started later this year. Because that work is not all very appealing, and I have lots of other work still on my plate, it's very easy to procrastinate on.

Separately, I ended up in a situation where I contractually had to take at least two weeks of leave, with something like six workweeks left in the year [!ask me about collective bargaining, our contract is wild!]. This made pretty much any amount of procrastination very dangerous!

I set up [a goal](https://www.beeminder.com/tris/2025q4sprint) tracking [pomodoros](https://www.pomodorotechnique.com/) to make sure I dedicate enough time to this type of work through the rest of the year. It is working, and you can tell by how close my datapoints are to the red line [!how "edge-skatey" I am, in Beeminder parlance!] that I actually need it. I'm currently using 25/5 pomodoro blocks here but may switch to tracking "mostly-focused hours," if I end up needing this again --- there are too many interruptions, and some tasks with iteration loops that take too long, to really properly use the pomodoro technique.

**I'm on the path to fixing my voice.** I have been voice training [!in case this is somehow your first exposure to me/my blog: I'm a trans woman, and your voice doesn't magically become more feminine with any of the usual medical interventions, you have to put sustained effort in!] for almost 9 years, on and off, but never had the motivation to actually switch over to using my new voice full-time even though I knew it'd likely be better for my long-term mental health. I set up a goal tracking "best-effort days:" I entered a 1 on days where (a) I fixed my voice live if I ever caught myself dropping out of it, and (b) spent at least a few minutes talking at all (some days are totally silent otherwise). I archived it pretty much immediately, because having the goal in place for just 3 days was enough to kick my muscle memory into the right place. I still have a long way to go, but this has been huge for me so far.

**I've learned a lot about myself as a result.** The boundaries of my motivation are way clearer to me. I am far more aware of how much time things take, and value my time more as a result. And most importantly, I'm starting to regain trust in myself; I'm relearning that I can *actually execute on things if I really want to.* [!This [blog post on "spiraling into control"](https://blog.beeminder.com/nick) matches my experience, though Nick is way more hardcore about it than I am!!]

## Caveats and learnings

Obviously this has been a huge success for me so far. There are a few reasons I don't think this would work for everyone, and a few things that I am still trying to solve, that seem worth talking about.

First and most importantly, **Beeminder messes with my motivation in an extremely powerful way.** That's the whole point, yes, but I realized pretty quickly that I have to be extremely mindful of second- and third-order effects of simply editing my motivations like this [!as in, short-circuiting the paths that usually put short-term motivations in my head!]. For example, my "focus on end-of-year job tasks" goal initially made me less responsive to work I have to do to unblock my coworkers. I adjusted the goal to give me more time in the day to do that kind of work, but realizing that I can simply override behavior patterns that I associate with deeply held values was and is still very scary.

More generally, if you can tell that Beeminder is going to be an effective commitment device, I think it's really important to start slowly and **be kind to yourself**. It's very easy for me to imagine a situation where I don't do enough reflection on my goals, and end up using Beeminder in a way that "crush parts of myself that I ought to be listening to more" [!Daniel's words, not mine, from the November 20th Beeminder newsletter!] or is otherwise self-destructive. Of course, I can solve this with another Beeminder goal --- forcing myself to journal nearly daily helps me to reflect early and often to catch problems like this!

When thinking about how to be kind to myself with my goals, the [want-can-will test](https://blog.beeminder.com/wantcanwill/) has been very helpful. If I'm not certain that I am physically or mentally able to do something at a certain pace, I won't beemind it at that pace (though I might start smaller and work my way up!). And I keep an eye on how well my actual "wants" match with my behavior as influenced by my Beeminder goals. Being very careful here makes using Beeminder way less scary than I initially assumed, though it does demand a lot of self-reflection.

I find it helpful and important to think about derailment payments [!potential derailments, really --- I hadn't derailed yet at publication time!] as a financial cost of all of the self-improvement you've done up to that point. If I thought about derailing as a "punishment" for "not doing enough," Beeminder would be far worse for my mental health. [Paying Is Not Punishment](https://blog.beeminder.com/depunish/) and [Derailing It Is Nailing It](https://blog.beeminder.com/nailingit) talk more about this philosophy and I think should be required reading before starting.

**Beeminder works so well for me because I am honest to a fault.** Any worries about cheating impacting my data evaporated when I realized that faking data in Beeminder was essentially just lying to myself, which I hate doing. Daniel writes more about this in [The Type Bee Personality](https://blog.beeminder.com/typebee). If this isn't you, Beeminder probably doesn't work.

**It's generally better to set goals on inputs, not outputs.** I've been avoiding beeminding things that I can't actually make progress on in a one-day period. For example, I sleep very light, so beeminding "hours slept" would probably be demotivating for a while. "Time I get out of bed" is something I can affect immediately, though, and I trust my body to eventually adjust my bedtime so I'm getting enough sleep. Same deal with work outcomes; it's better for my motivation to beemind focus time because I'm often wrong when estimating how long something takes.

As I learn to trust myself again, some of these things (like journaling) are becoming habits, but I still feel **Beeminder is still an important backstop for my motivation.** It's easier for me to just do something (and not constantly worry about whether or not I'll keep maintaining the habit of doing that thing) when I know that I'll essentially be forced back into it should I fall out of it for too long. That's weird and circular, but it's how my brain works.

## Open questions

* Can I beemind individual tasks? The answer is probably yes, using [The One Must-Do Task Each Day](https://blog.beeminder.com/mustdo/) mechanism, [TaskRatchet](https://taskratchet.com/), or [Intend](https://intend.do)'s commitment contracts, but how do I make sure to do this in a healthy way?
* How should I make more creative output happen (photography, blog posts, maybe something else...?) with this framework?
