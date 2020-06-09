from database.db import db
from mongoengine import StringField


class User(db.Document):
    name = StringField(required=True)
