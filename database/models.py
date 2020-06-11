import datetime
from database.db import db
from mongoengine import *


class Reported_Item(db.EmbeddedDocument):
    item_id = StringField()
    item_type = StringField()


class Reported_Users(db.Document):
    user_id = StringField(required=True)
    name = StringField(required=True, unique=True)
    modified = DateTimeField(default=datetime.datetime.now)
    reported_items = ListField(
        EmbeddedDocumentField(Reported_Item), required=True)
