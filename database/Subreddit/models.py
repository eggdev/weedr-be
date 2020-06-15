from database.db import db
from mongoengine import Document, StringField, ListField
from pprint import pprint


class Subreddit(Document):
    sr = StringField(required=True)
    reported_submissions = ListField(required=False)
    reported_comments = ListField(required=False)

    def add_reported_item(self, items, item_type):
        for item in items:
            item_list = self.reported_comments if item_type == 'comment' else self.reported_submissions
            if not item.id in item_list:
                item_list.append(item.id)
