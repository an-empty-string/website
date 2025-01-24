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
    return render_template("index.html")


@app.route("/bookmarks.html")
def bookmarks():
    return render_template("bookmarks.html")


@app.route("/speedrun/")
def speedrun():
    return render_template("speedrun.html")


def all_posts():
    posts = []

    for post in os.listdir("posts"):
        if not post.endswith(".md"):
            continue

        slug = post.removesuffix(".md")
        with open(f"posts/{post}") as f:
            content = f.read()
            _, raw_meta, _ = content.split("---\n")
            meta = yaml.safe_load(raw_meta)
            posts.append((slug, meta))

    posts.sort(key=lambda pm: pm[1]["posted_on"], reverse=True)
    return posts


@app.route("/blog/")
@app.route("/blog/index.html")
def blog():
    posts = all_posts()
    posts = itertools.groupby(posts, key=lambda pm: pm[1]["posted_on"].year)
    return render_template("blog.html", posts=posts)


@app.route("/blog/rss.xml")
def rss():
    return render_template("rss.xml", posts=all_posts())


@app.route("/blog/<slug>.html")
def post(slug):
    try:
        with open(f"posts/{slug}.md") as f:
            content = f.read()
            _, raw_meta, post = content.split("---\n")
            meta = yaml.safe_load(raw_meta)

    except FileNotFoundError:
        abort(404)

    md = markdown.Markdown(
        extensions=[
            "fenced_code",
            "codehilite",
            "toc",
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
