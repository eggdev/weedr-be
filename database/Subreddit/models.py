from database.db import db
from mongoengine import Document, StringField, ListField


class Subreddit(Document):
    sr = StringField(required=True)
    reported_submissions = ListField(required=True)
    reported_comments = ListField(required=True)
    authors = ListField(required=True)

    def add_reported_item(self, item, item_type):
        item_list = self.reported_comments if item_type == 'comment' else self.reported_submissions
        print(item.author)
