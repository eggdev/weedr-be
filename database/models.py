import datetime
from database.db import db
from mongoengine import StringField, ListField, DateTimeField, ObjectIdField


class Reported_Users(db.Document):
    redditor_id = StringField(required=[True])
    name = StringField(required=True)
    modified = DateTimeField(default=datetime.datetime.now)
    reported_items = ListField(StringField(required=True), required=True)
