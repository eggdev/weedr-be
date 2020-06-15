from database.db import db
from mongoengine import Document, StringField, ListField
from utils.helpers import generate_json_from_praw


class Redditor(Document):
    username = StringField(required=True)
    reported_items = ListField(required=False)

    def add_reported_item(self, item):
        if not item.id in self.reported_items:
            self.reported_items.append(item.id)
