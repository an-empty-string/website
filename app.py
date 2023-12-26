import itertools
import os

import markdown
import yaml
from flask import Flask, abort, render_template

app = Flask(__name__)
app.config["SERVER_NAME"] = "tris.fyi"


@app.route("/")
@app.route("/index.html")
def index():
    return render_template("index.html")


@app.route("/bookmarks.html")
def bookmarks():
    return render_template("bookmarks.html")


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

    post = post.replace(" [!", '<span class="sidenote"><small>')
    post = post.replace("!]", "</small><button>(show note)</button></span>")

    html_post = md.convert(post)
    return render_template(
        "post.html", meta=meta, post=html_post, toc=getattr(md, "toc", None)
    )


if __name__ == "__main__":
    app.run(port=5050, debug=True)
