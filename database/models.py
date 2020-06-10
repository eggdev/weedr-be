from database.db import db
from mongoengine import StringField, ListField, ObjectIdField


class Reported_Users(db.Document):
    name = StringField(required=True)
    # reported_items = ListField(required=True)
    # redditor_data = ObjectIdField(require=True)
    # redditor_data =
