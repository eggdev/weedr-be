from database.db import db
from mongoengine import Document, StringField, ListField
from pprint import pprint


class Subreddit(Document):
    sr = StringField(required=True)
    reported_items = ListField(required=False)
    reported_users = ListField(required=False)

    def add_reported_items(self, items):
        for item in items:
            if not item.author.name in self.reported_users:
                self.reported_users.append(item.author.name)
            if not item.id in self.reported_items:
                self.reported_items.append(item.id)

    def make_return_object(self, subreddit):
        return {"subreddit": self.sr}
