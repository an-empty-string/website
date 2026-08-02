import itertools
import operator
import os
import uuid
from typing import Iterator

import markdown
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


def render_markdown(text):
    md = markdown.Markdown(
        extensions=[
            "fenced_code",
            "codehilite",
            "toc",
            "pymdownx.blocks.details",
            "pymdownx.blocks.html",
            "pymdownx.emoji",
        ]
    )

    lines = text.split("\n")
    in_code_block = False
    transformed_lines = []

    for line in lines:
        if line.startswith("```"):
            in_code_block = not in_code_block

        line = line.replace(" --- ", " &mdash; ")

        if not in_code_block:
            line = line.replace("...", "&hellip;")

        transformed_lines.append(line)

    text = "\n".join(transformed_lines)

    return md, md.convert(text)


def parse_markdown_file_with_frontmatter(filename):
    slug_candidate = os.path.basename(filename).removesuffix(".md")

    props = {
        "slug": slug_candidate,  # overwritten with slug from frontmatter
    }

    with open(filename) as f:
        content = f.read()

        _, raw_frontmatter, content = content.split("---\n", maxsplit=2)
        frontmatter = yaml.safe_load(raw_frontmatter)

        props.update(frontmatter)
        props["content"] = content

        # bunch of special casing for blog posts
        content = content.replace(" [!", '<span class="sidenote"><small>')
        content = content.replace("!]", "</small></span>")

        md_renderer, html_content = render_markdown(content)

        props["html_renderer"] = md_renderer
        props["html_content"] = html_content

    return props


def assign_missing_ids(x):
    x["order"] = next(order)

    if "id" in x:
        return x

    if "url" in x:
        x["id"] = uuid.uuid3(uuid.NAMESPACE_URL, x["url"])
        return x

    if "slug" in x:
        x["id"] = uuid.uuid3(uuid.NAMESPACE_URL, f"trisfyi:slug:{x['slug']}")
        return x

    raise ValueError(f"Could not assign IDs to item {x!r}")


def collect_items(path="items", assign_ids=True, assign_type=None) -> list[dict]:
    items = []

    for dirpath, dirnames, filenames in os.walk(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), path)
    ):
        dirnames.sort()

        for filename in sorted(filenames):
            if filename.endswith(".md"):
                items.append(
                    parse_markdown_file_with_frontmatter(
                        os.path.join(dirpath, filename)
                    )
                )

            if not filename.endswith(".yaml"):
                continue

            with open(os.path.join(dirpath, filename)) as f:
                items.extend(parse_items(yaml.safe_load(f)))

    if assign_ids:
        items = [assign_missing_ids(x) for x in items]

    if assign_type:
        for item in items:
            item["type"] = assign_type

    return items


def collect_all_items():
    return collect_items() + collect_items("posts", assign_type="post")


def find_items(typ, tags=None, order_by="order", only_these_keys=None):
    if tags is None:
        tags = []

    items = []

    for item in collect_all_items():
        if item["type"] != typ:
            continue

        if not all(x in item.get("tags", []) for x in tags):
            continue

        items.append(item)

    items.sort(key=operator.itemgetter(order_by))

    if only_these_keys:
        items = [{k: v for k, v in x.items() if k in only_these_keys} for x in items]

    return items
