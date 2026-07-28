import collections
import itertools
import os

import markdown
import yaml
from flask import Flask, abort, render_template

import items

app = Flask(__name__)
if not os.getenv("LOCAL"):
    app.config["SERVER_NAME"] = "tris.fyi"


@app.route("/")
@app.route("/index.html")
def index():
    return render_template("index.html", posts=all_posts())


@app.route("/bookmarks.html")
def bookmarks():
    return render_template("bookmarks.html")


@app.route("/elect.html")
def elect():
    return render_template("elect.html")


@app.route("/speedrun/")
def speedrun():
    return render_template("speedrun.html")


# Blog rendering
def all_posts(include_private=False):
    posts = items.find_items("post", order_by="posted_on")[::-1]

    if not include_private:
        posts = [p for p in posts if "private_uuid" not in p]

    return posts


def get_post_by_slug(slug):
    posts = all_posts(include_private=True)
    for p in posts:
        if p["slug"] == slug:
            return p


@app.route("/blog/")
@app.route("/blog/index.html")
def blog():
    posts = all_posts()
    posts = itertools.groupby(posts, key=lambda p: p["posted_on"].year)
    return render_template("blog.html", posts=posts)


@app.route("/blog/rss.xml")
def rss():
    resp = render_template("rss.xml", posts=all_posts())

    # for ease of viewing - not used when rendered, really
    return resp, {"Content-Type": "text/plain"}


@app.route("/blog/<slug>.html")
@app.route("/blog/<slug>/<private_uuid>.html")
def post(slug, private_uuid=None):
    post_data = get_post_by_slug(slug)
    if post_data is None:
        abort(404)

    if post_data.get("private_uuid") != private_uuid:
        abort(404)

    html_post = post_data.pop("html_content")
    toc = getattr(post_data.pop("html_renderer"), "toc", None)

    has_sidenotes = '<span class="sidenote">' in html_post

    if not os.getenv("LOCAL"):
        html_post = html_post.replace(
            "/static/blog/", "https://cdn.tris.fyi/static/blog/"
        )

    return render_template(
        "post.html",
        meta=post_data,
        post=html_post,
        toc=toc,
        has_sidenotes=has_sidenotes,
    )


# items framework {{{
def render_markdown_with_link_shorthand(text, item):
    assert "title" in item
    assert "url" in item

    item_title = item["title"]
    if "author" in item:
        item_title = f"{item['author']} --- {item['title']}"

    text = text.replace("<>", "[]()")
    text = text.replace("[]", f"[{item_title}]")
    text = text.replace("()", f"({item['url']})")

    _, html = items.render_markdown(text)

    html = html.removeprefix("<p>").removesuffix("</p>")
    return html


@app.context_processor
def inject_item_helpers():
    return {
        "find_items": items.find_items,
        "render_markdown_with_link_shorthand": render_markdown_with_link_shorthand,
    }


# }}}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5051, debug=True)
