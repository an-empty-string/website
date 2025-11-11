---
title: asr2geojson
subtitle: a tool for making FCC Antenna Structure Registration data usable
summary: how to plot nearly every antenna structure in the US on a map in (n) easy steps!
posted_on: 2024-03-18
show_toc: false
---

Have you ever wanted to know who owns that tower near your apartment building? Or have you ever thought "wow, I sure wish I could visit a cool antenna structure near me this weekend"?

If you answered "no," congratulations, you're normal! If you answered "yes," then I have just the tool for you.

The FCC requires registration and approval for most antenna structures constructed in the United States, through the [Antenna Structure Registration](https://www.fcc.gov/wireless/support/knowledge-base/antenna-structure-registration-asr-resources/antenna-structure) process. Since the FCC is a federal entity, these registrations are available under the Freedom of Information Act; the Commission publishes a snapshot of their entire database weekly as [Public Access Files](https://www.fcc.gov/wireless/data/public-access-files-database-downloads).

Digging into these files, it's difficult to immediately do anything with them: coordinates, tower height, and ownership data are in different files. Files are pipe-delimited and a bit painful to parse (for example, some records contain newlines). I wrote [asr2geojson](https://github.com/an-empty-string/asr2geojson) to convert these files to several formats. Running `make` in a checkout of this repository gives you:

* a SpatiaLite database with a single table containing coordinates, tower height, and owning entity information, indexed spatially (load this into QGIS and you're immediately able to see towers near you)
* a GeoJSON file with the same information for interchange with other systems
* a SQLite database with a schema that mirrors the FCC's (see `schema.sql`)
