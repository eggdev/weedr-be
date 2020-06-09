# {DB_HOST}://{DB_USERNAME}:{DB_PASSWORD}@{DB_PORT}/{DB_COLLECTION}/{SUBREDDIT}?retryWrites=true&w=majority
from flask_mongoengine import MongoEngine

db = MongoEngine()


def initialize_db(app):
    db.init_app(app)
