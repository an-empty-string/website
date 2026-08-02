from flask_frozen import Freezer

from app import all_posts, app

freezer = Freezer(app)


@freezer.register_generator
def post():
    for post in all_posts(True):
        if "private_uuid" in post:
            yield {"slug": post["slug"], "private_uuid": post["private_uuid"]}

        else:
            yield {"slug": post["slug"]}


if __name__ == "__main__":
    freezer.freeze()
