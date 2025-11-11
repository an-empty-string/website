from flask_frozen import Freezer

from app import all_posts, app

freezer = Freezer(app)


@freezer.register_generator
def post():
    for slug, meta in all_posts(True):
        if "private_uuid" in meta:
            yield {"slug": slug, "private_uuid": meta["private_uuid"]}

        else:
            yield {"slug": slug}


if __name__ == "__main__":
    freezer.freeze()
