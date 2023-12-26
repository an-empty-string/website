---
title: 2021 Advent of Code retrospective
summary: "Musings on the 2021 Advent of Code event: how I played, what I thought about the puzzles, my plans for 2022."
posted_on: 2021-12-24
---

This year, I participated in Eric Wastl's [Advent of Code](https://adventofcode.com), as I have done in past years. I had a lot of fun and will definitely play again in the next event. This post is about lessons I learned this year and what I would like to differently next year.

## How I played

As usual, I wrote my solutions in Python with a custom answer download and submission framework. I'd like to clean this up and release the framework, but I don't really have the time or motivation right now.

Unlike past years, I tried to write some reusable utility functions throughout the event. I ended up with a few useful ones, but I usually didn't reuse them for more than one day. Utility functions are covered a bit more later.

As for how I performed during the event—I think I did really well! Just from December 1st to 23rd I managed to get 40 out of 50 stars, which is significantly better than I've done in previous years. I also placed 33rd on the global leaderboard. At the time of writing, there were over 210k people who got the first star in the event. Of course, not all of them were playing competitively, but I'm still very proud of how I performed this time around!

In past years, I've been competitive on the leaderboard, but burnt out around day 10 from the stress of trying to stay competitive. This year, I managed to hold on through Day 22 (although I didn't complete every puzzle). I think I burnt out this year just from not having enough energy to quickly complete 25 multipart programming puzzles in a row, instead of pressure to compete.

## Thoughts on the puzzles

I think Eric did a great job with the difficulty curve this year, although the ramp-up on day 19 was a bit much for me. Days 22 and 23 also had very rough second parts compared to their first parts. I don't think these are a bad thing, it was just difficult to get used to when the first 18 days had a more consistent difficulty curve.

## Plans for next year

I will definitely be playing Advent of Code next December if I am able to. I don't know if I'll play for global leaderboard placement though—it was very stressful, and "having" to solve problems quickly definitely negatively impacted my enjoyment of the event.

Next year, I'd like to try to focus on well-designed and tested solutions, instead of quick and dirty code. This would make it much easier to release my work and let me keep a healthy sleep schedule, too :)

If I play competitively again, I'll write a more comprehensive utility library well in advance. These themes came up during this event:

* Finding neighboring coordinates on a plane or cube
* Sliding window (1-dimensional case of neighbors)
* Doing other stuff on 2D grids (evaluating rows and columns, displaying state, folding the grid)
* Finding intersections and differences of planes and cubes
* Rotating objects in space, translating coordinates
* Directed and undirected graph search (A*)
* Restricted graph traversal (paths must satisfy a predicate)
* Flood fill (I think having a working BFS is enough for this)
* Permutations
* Tree traversal
* Dynamic programming and memoization
* Lists of instructions (command followed by some arguments) mutating some state
* Binary parsing
* Reverse engineering (some kind of generic symbolic execution engine would be really useful, maybe keep an eye out for a "learning angr to solve Day 24" blog post...? maybe not)
* Counting states and using state counts (instead of a list of states) to compute a next set of states (Day 6)
* Cellular automata, maybe? I'm thinking of days 14 and 20 here.

Plus, of course, the usual input parsing requirements. It would be nice to have a better way to parse inputs next year, but I'm not sure how this would look.

## Final thoughts

I had a good time playing and solving the puzzles this year! Thanks to Eric and everyone else who made Advent of Code happen this year.

Thanks also to the folks in #adventofcode and #adventofcode-spoilers on Libera.Chat for talking about optimization with me and for pointing out how I made some of my algorithms accidentally take way longer than they should :)

Looking forward to next year!
