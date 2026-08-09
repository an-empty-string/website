import os

from flask_frozen import Freezer

from app import all_posts, app

os.environ["FREEZE"] = "1"

freezer = Freezer(app)


@freezer.register_generator
def post():
    for post in all_posts(True):
        if "private_uuid" in post:
            print("private post", post["slug"], post["private_uuid"])
            yield {"slug": post["slug"], "private_uuid": post["private_uuid"]}

        else:
            print("post", post["slug"])
            yield {"slug": post["slug"]}


if __name__ == "__main__":
    freezer.freeze()
