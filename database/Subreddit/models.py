import datetime
from database.db import db
from mongoengine import Document, StringField, ListField


# All lists will be references to other DB Objects
class Subreddit(Document):
    name = StringField(required=True)
    moderators = ListField(required=True)
    comments = ListField(required=True)
    submissions = ListField(required=True)
    redditors = ListField(required=True)
