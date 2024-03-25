from flask_frozen import Freezer

from app import all_posts, app

freezer = Freezer(app)


@freezer.register_generator
def post():
    for slug, _ in all_posts():
        yield {"slug": slug}


if __name__ == "__main__":
    freezer.freeze()
