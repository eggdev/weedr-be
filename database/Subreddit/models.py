from database.db import db
from mongoengine import Document, StringField, ListField
from pprint import pprint


class Subreddit(Document):
    sr = StringField(required=True)
    reported_items = ListField(required=False)

    def add_reported_items(self, items):
        for item in items:
            if not item.id in self.reported_items:
                self.reported_items.append(item.id)
