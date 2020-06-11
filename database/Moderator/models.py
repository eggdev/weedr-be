import datetime
from database.db import db
from mongoengine import Document, StringField, ListField


class Moderator(Document):
    username = StringField(required=True)
    password = StringField(required=True)
    subreddits = ListField(required=True)
