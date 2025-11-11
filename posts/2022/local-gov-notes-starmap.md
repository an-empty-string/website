---
title: Huntsville local government-related project starmap
summary: A list of projects I was once working on to keep track of Huntsville local government.
posted_on: 2022-09-19
updated_on: 2023-12-19
---

This page lists long-term projects that are related to my Huntsville, AL government work (policy advocacy, transparency, or anything else). Since I don't live in Huntsville anymore, a lot of these projects are on hold indefinitely, but if you're interested in further details about any of these projects (because you want to try them yourself, or otherwise), please reach out!

It's called a "starmap" because calling it a "roadmap" would imply that I've made detailed plans on how to complete each of these projects. That is not the case &ndash; at the time of writing, most of these projects have very little planning or implementation work behind them.

If you have an idea for one of these projects, or want to help make them a reality, please please contact me via email at tris@tris.fyi.

## Preliminary Agenda Tool

The most complete project on this page! [Available here](https://tris.fyi/agenda.html), it shows you items on upcoming city council agendas before they are made final.

This is possible because Legistar (the city's agenda tracking tool) has an [API](https://webapi.legistar.com/Help) which exposes more information than is made available in the [calendar view](https://huntsvilleal.legistar.com/Calendar.aspx). None of the information on the preliminary agenda tool is non-public &ndash; all I'm doing is presenting public information in a more easily digestable form.

Happy to share code if you're interested; eventually I'll also clean it up and publish it on GitHub (as will hopefully be the case with every project here).

## Finance Data Parser

Every two weeks, the finance department submits a long PDF document containing details about every expense paid to a vendor by the city (among other things). The goal here is to parse out this data from the PDFs and append it to a SQLite database for consumption via [Datasette](https://datasette.io/).

For this to be the most useful, we will also need a mapping of account numbers to city departments so we know who is spending what.

## Interchange Specs

Well-defined interoperable formats for data about government actions. I wrote some draft specs (unpublished) for this; if you're interested in what they look like please reach out. I don't think they are suitable for use in their current form, otherwise I'd publish them here.

## City Action Tracking System

...or "cats" for short (ahaha) is my grand vision of a unified database for tracking all actions/decisions made by any boards/commissions/councils in the city.

### Entities

The most important/groundbreaking thing about this project is its ability to track relationships between lots of entities (as envisioned in [this tweet](https://twitter.com/an_empty_string/status/1543788525996343303/photo/1)). An explanation of this diagram is as follows. It is very dense, so sorry about that:

* A **Body** is a generalization of a board, commission, or council: any group of two or more _people_ that holds _meetings_ to deliberate and make decisions on _matters_, via _actions_. The form of _actions_ usually are based on some kind of parliamentary authority (in Huntsville, city council has adopted Robert's Rules, for example).
* _Bodies_ of course consist of **Person**s. Each person may hold zero or more _positions_ on a body (like "President" or "Chair"); usually each _body_ will decide which of their members will hold which _positions_.
    * Persons more generally represent anyone in city government &ndash; Tommy Battle is a person who holds the _office_ of Mayor; Thomas Nunez is a person who has an _affiliation_ with the Planning Department (represented as an _organization_ in this model).
* Every _person_ serving on a _body_ sits on exactly one **Seat** &ndash; think council district or "place number" defined in formation ordinances. Seats are either elected or have an appointment authority (another _body_ can make appointments, or the appointment can be made by an _office_ like "Mayor" &ndash; although ultimately it's still _persons_ making appointments, they just hold an _office_ or a vote through their seat on a _body_).
* The combination of _person_, _seat_, _positions_, and _body_ (transitively) defines a **Membership**. Memberships are queryable by time, so by looking through a _person_'s memberships, for a given _body_, you can see what _positions_ they held in the past, for example.
* A **Matter** is a document that a _body_ deliberates on. This is usually a resolution or ordinance.
    * Matters can be defined as relating to other matters without additional context (e.g. ordinances which amend other ordinances, or relating a zoning ordinance amendment coming before city council to its planning commission recommendation).
    * Matters can also be part of a _project_ (representing collections of ordinances which might not seem related on first look, but are related to the same activity, like an economic development project).
    * Matters also have a _matter category_, like "rezoning request", "annexation", "subdivision approval", or "contract approval".
    * Matters can optionally have _additional matter data_, which might represent the total size of an annexation, the parcel number related to a rezoning request, or similar.
    * _Projects_, _matter categories_, and _additional matter data_ are not represented in the diagram linked above.
* A _body_ holds **Meeting**s (which can be of different _meeting types_, like "regular session", "work session", or "special session"), almost always with a formal agenda (consisting of _agenda items_ describing the _matters_ to come before the body in the meeting). The meeting is usually conducted physically at a _location_ (this is often required by bylaws), although some meetings are held online only.
* At a _meeting_, the _body_ considers _matters_ and takes **Action**s on them. These actions are usually voted on by each _person_ on the _body_; these votes are recorded as **ActionVote**s.

### Notes

Notes can be taken on most objects in the system (although the diagram linked above only shows the potential to take notes on _agenda items_ and _matters_).

At first, notes will probably be fairly limited, but I'd like to develop a system where you can sign in and take private notes (on agenda items / people / meetings / matters / actions / votes). Then, later, you could share these notes within a group (like a citizen journalism organization, or a group doing advocacy for a particular cause) or publicly.

This collaboration functionality has potential for abuse and needs a lot more risk analysis / control design before making it widely available.

### Possibilities

All the relationships between entities described above are queryable (at least at a database level), so you can answer questions like this:

* Who on planning commission has abstained from voting on subdivision requests recently?
* What were the most controversial measures (by difference between yes and no votes) that ultimately passed (or failed)?
* What did the zoning subcommittee (of planning commission) have to say about this proposed zoning ordinance amendment?
* Do annexations further from the city center fail more often? (through consistent PPIN tracking and a little bit of GIS work)

And more boring questions:

* When and where does this commission meet next?
* What items are on the agenda for this board?

### Other possibilities

* Audio/video recording integration and agenda item timecoding

## Zoning Explorer

What if we the zoning ordinance was machine-readable? We'd be able to easily answer questions like:

* What uses are allowed in Residence 2-A zoning that aren't allowed in Residence 2 zoning?
* What's the difference in density requirements between two zones? (yard setbacks, minimum lot sizes, etc)
* Where else is a specific use permitted? (And when does that use need a special exception from the Board of Zoning Adjustment vs. a variance?)

Also, with a bit of GIS work (and consistent PPIN tracking on Board of Zoning Adjustment actions, and potentially some integration with the probate court deed filing system), we could track this data and answer these questions at the property level:

* What variances are active for a given property? (And what uses do those variances permit, exactly?)
* Which variances have lapsed due to ownership changes?

## Text Explorer

A generalization of Zoning Explorer:

* a way to search the full text of every ordinance and resolution passed by any governing body
* ...and policies/procedures followed by other bodies (like the police department's written directives)
* a uniform, non-proprietary citation format that's specific enough to reference individual paragraphs/lines in a specific code version, ordinances, or resolutions
* mostly-automatic updates after council meetings, including automatic linking between documents

Some considerations here:

* not duplicating existing work in uniform citation systems
* being able to site state codes, US code, congressional acts, and case law
