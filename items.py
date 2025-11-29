import itertools
import operator
import os
import uuid
from typing import Iterator

import yaml

order = itertools.count()


def parse_items(xs, props=None) -> Iterator[dict]:
    if props is None:
        props = {}

    assert isinstance(xs, (dict, list))

    if isinstance(xs, dict):
        if "items" in xs:
            items = xs.pop("items")
            yield from parse_items(items, props=xs)

        else:
            yield xs | props

    elif isinstance(xs, list):
        for item in xs:
            yield from parse_items(item, props)


def assign_missing_ids(x):
    x["order"] = next(order)

    if "id" in x:
        return x

    if "url" in x:
        x["id"] = uuid.uuid3(uuid.NAMESPACE_URL, x["url"])
        return x

    raise ValueError(f"Could not assign IDs to item {x!r}")


def collect_items() -> list[dict]:
    items = []

    for dirpath, dirnames, filenames in os.walk(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "items")
    ):
        dirnames.sort()

        for filename in sorted(filenames):
            if not filename.endswith(".yaml"):
                continue

            with open(os.path.join(dirpath, filename)) as f:
                items.extend(parse_items(yaml.safe_load(f)))

    items = [assign_missing_ids(x) for x in items]
    return items


def find_items(typ, tags=None):
    if tags is None:
        tags = []

    items = []

    for item in collect_items():
        if item["type"] != typ:
            continue

        if not all(x in item.get("tags", []) for x in tags):
            continue

        items.append(item)

    items.sort(key=operator.itemgetter("order"))
    return items
