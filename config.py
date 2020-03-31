import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL"
    ) or "sqlite:///" + os.path.join(BASE_DIR, "db.sqlite")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
