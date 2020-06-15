from database.db import db
from mongoengine import Document, StringField, ListField
from utils.helpers import generate_json_from_praw


class Redditor(Document):
    username = StringField(required=True)
    reported_submissions = ListField(required=True)
    reported_comments = ListField(required=True)

    def add_reported_item(self, item, item_type):
        item_list = self.reported_comments if item_type == 'comment' else self.reported_submissions
        item_obj = {
            "subreddit": item.subreddit,
            "post_id": item.id,
        }
        print(item_obj)
