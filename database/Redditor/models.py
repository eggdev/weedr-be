from database.db import db
from mongoengine import Document, StringField, ListField


class Redditor(Document):
    username = StringField(required=True)
    reported_submissions = ListField(required=True)
    reported_comments = ListField(required=True)

    def generate_new(self, item, item_type):
        print(item)

    def add_new_item(self, item, item_type):
        print(item)
