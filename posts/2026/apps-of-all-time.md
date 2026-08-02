---
title: Apps of all time
posted_on: 2026-08-02
show_toc: false
featured: true
---

Here are some tools I find useful, or have found useful at some point in the past. I'll likely update this regularly as I think of more things.

# Software

## VisiData

Sometimes I have a CSV file, or a SQLite database, or a big JSON blob, or an Excel spreadsheet, or... you get the gist. I've got a lot of data, and I don't really know what to make of it just yet.

The tool I usually reach for is [VisiData](https://www.visidata.org/). VisiData lets you do a whole lot with tabular data, including:

* Frequency tables and aggregation! For example, if I have a log file listing individual HTTP requests, each with a URL and processing time, I can use create a "sum" aggregator on the processing time column, then group by URL just by putting my cursor in the column and hitting "F". I almost immediately get a table of URLs with their total processing time. See [Grouping data and descriptive statistics from the VisiData docs](https://www.visidata.org/docs/group/) for more about this.
* Creating new columns, with values coming from Python expressions operating on other columns - `=`. (So, it works like a traditional spreadsheet, too!)
* [Graphing](https://www.visidata.org/docs/graph/) in the terminal!
* Creating ad-hoc data processing pipelines using its [cmdlog](https://www.visidata.org/docs/save-restore/) functionality.

## Rowboat

If I have a CSV file with a ton of columns, I'll throw it into [Rowboat](https://rowboat.net/) so I can visualize distributions of many columns at once. It also lets you do filtering by clicking and dragging over columns, which is really intuitive! It's written in something that compiles to WebAssembly, or something like that; it's ridiculously fast.

## QGIS

I come across geospatial data that I want to dig into far more frequently than the average person, I think. After doing a bunch of zoning code exploration as part of an old local government watching hobby, I picked up [QGIS](https://www.qgis.org/), since it's the most full-featured free software GIS tooling available. (ArcGIS is the industry standard, but I'm not about to pay for a license!)

Anyway, being able to pull datasets from ArcGIS-compatible endpoints (search "arcgis" on [my bookmarks page](/bookmarks.html)) and visualize arbitrary combinations of datasets with arbitrary coloring rules is already huge, and gets you way further than what most people are able to do with e.g. [city web mapping tools](https://maps.huntsvilleal.gov).

The ability to do spatial joins across datasets, georeference PDF maps and display them alongside other layers, and import your own datasets (even CSVs) basically gives you superpowers.

Learning QGIS was well worth the time for me!

## OurGroceries

I have a very particular problem. If I store my grocery lists in a generic tool like Google Keep, I end up with a triple-digit number of grocery lists, none of which actually represent what I need to buy. Having a place to put grocery lists, and only grocery lists, fixes this!

[OurGroceries](https://ourgroceries.com/) provides this. It also provides auto-categorization of items (corresponding roughly to aisles or areas in the grocery store), which speeds up my trips a lot! And if you're going shopping with a partner, every client looking at the same list syncs in real-time, so you can efficiently e.g. start on opposite sides of the store and meet in the middle.

I only want for a Pebble app... There is no official API so this would take some reverse engineering, I think.

## YNAB

[YNAB](https://ynab.com) lets me understand my financial situation quite a lot better than I otherwise would, and is the best tool I've found to do that in a way that is compatible with my brain.

YNAB implements "envelope budgeting" or "zero-based" budgeting, which basically means that whenever you get paid, you put your new money in envelopes ("categories"), which you spend out of for specific things. I have over 60 categories in my budget right now, between savings goals, charitable giving, fixed monthly expenses (like rent, and smaller subscription services), and variable expenses (like groceries and travel). YNAB gives me the space to be intentional about what I am putting my money towards without having to keep it all in my head.

## Beeminder

I [wrote about Beeminder before](/blog/one-month-with-beeminder.html); I still use it. At the time of writing, I'm using it to help me keep my apartment tidy, go to sleep on time, maintain a daily journal, keep this website fresh (I'm writing this post because my "website touches" goal went red!), cook at home consistently, and read consistently. It's still the only thing I've found that actually works.

I'm looking at [TaskRatchet](https://taskratchet.com/) to help with less habit-shaped things, but haven't adopted it yet.

## Taskwarrior

[Taskwarrior](https://taskwarrior.org/) is probably the most flexible to-do list system in existence. Unfortunately, this flexibility was my downfall; I no longer use it because my brain wanted to spend more time customizing the workflow than actually working with it. It also doesn't have a great mobile app story.

These days I track my todos in Todoist instead, but I often wish I had the flexibility that Taskwarrior gave me...

# Physical objects

## Anker 65W charger

[This charger](https://www.anker.com/products/a2667?variant=41581366575254) is the only one I ever carry when I am traveling, along with a couple of power measuring USB cables. It is small and light enough that it fits inside those cables when coiled without any trouble. It is powerful enough to charge my laptop and phone at the same time. And these days it is cheap enough ($25) to replace if I lose it.

## Toshiba 3-cup rice cooker

I used to be really disappointed with rice cookers until I got a [TRCS02](https://www.toshiba-lifestyle.com/us/all-cooking-appliances/rice-cookers/3-cup-uncooked-digital-rice-cooker). This thing will cook a half-cup of rice without complaining, which is great when I'm often cooking for just myself. And it makes the best rice I have ever tasted, hands down. I don't order rice when I get takeout anymore, I just make it at home.

## KitchenAid Classic stand mixer

[You know the one.](https://www.kitchenaid.com/countertop-appliances/stand-mixers/tilt-head-stand-mixers/p.classic-series-4-5-quart-tilt-head-stand-mixer.K45SSWH.html) It's often much cheaper used, and the quality is good enough that you aren't really missing out on anything if you buy it used.

The whisk attachment it comes with is great for breaking up and mixing berries into things, e.g. for raspberry pancakes.

The dough hook has made me so lazy about kneading. I never knead bread by hand in my kitchen anymore, unless I'm making [these dinner rolls](/blog/dinner-rolls.html).

It works well, it doesn't complain, it isn't connected to the internet; it's hard to not love. One of my favorite Kitchen Objects.

## Literally any Lodge cast iron

I know cast iron can be kind of polarizing, and for good reason! It is not trivial to clean like nonstick pans might be, and depending on how often and what you cook with it, you might have to season it now and then.

But also, it works!!! The relatively even heating + great heat retention makes things so much easier and more consistent.

Give me a [12" skillet](https://www.lodgecastiron.com/products/12-inch-cast-iron-skillet-with-handle-holder) and enameled dutch oven of reasonable size (6qt is what I have in my kitchen) and I can make basically anything.

## Pens and pencils

* The [Uni-ball Signo 0.38mm](https://www.jetpens.com/Uni-ball-Signo-UM-151-Gel-Pen-0.38-mm-Black/pd/306) has served me very well, though it's a little scratchy. I like that, but you might not.
* In my opinion, the [Pentel Twist-Erase](https://www.jetpens.com/Pentel-Twist-Erase-III-Mechanical-Pencil-0.5-mm-Violet-Body/pd/9251) is the most practical mechanical pencil on the market if you make a lot of mistakes, like I do.

I carry around at least one of each with me most places I go.
