import collections
import itertools
import os

import markdown
import yaml
from flask import Flask, abort, render_template

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


@app.route("/speedrun/")
def speedrun():
    return render_template("speedrun.html")


Post = collections.namedtuple("Post", ["slug", "meta", "content"])


def all_posts(include_private=False):
    posts = []

    for post_dir, _, post_filenames in os.walk("posts", followlinks=True):
        for post in post_filenames:
            if not post.endswith(".md"):
                continue

            slug = post.removesuffix(".md")
            with open(os.path.join(post_dir, post)) as f:
                content = f.read()
                _, raw_meta, post_content = content.split("---\n", maxsplit=2)
                meta = yaml.safe_load(raw_meta)

                if "slug" in meta:
                    slug = meta["slug"]

                if not include_private and "private_uuid" in meta:
                    continue

                posts.append(Post(slug, meta, post_content))

    posts.sort(key=lambda pm: pm[1]["posted_on"], reverse=True)
    return posts


def get_post_by_slug(slug):
    posts = all_posts(include_private=True)
    for post in posts:
        if post.slug == slug:
            return post


@app.route("/blog/")
@app.route("/blog/index.html")
def blog():
    posts = all_posts()
    posts = itertools.groupby(posts, key=lambda pm: pm.meta["posted_on"].year)
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

    _, meta, post = post_data

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

    olen = len(post)

    post = post.replace(" [!", '<span class="sidenote"><small>')
    post = post.replace("!]", "</small></span>")

    if not os.getenv("LOCAL"):
        post = post.replace("/static/blog/", "https://cdn.tris.fyi/static/blog/")

    has_sidenotes = len(post) != olen

    html_post = md.convert(post)
    return render_template(
        "post.html",
        meta=meta,
        post=html_post,
        toc=getattr(md, "toc", None),
        has_sidenotes=has_sidenotes,
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5051, debug=True)
