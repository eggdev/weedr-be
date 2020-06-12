import datetime
from database.db import db
from mongoengine import Document, StringField, ListField


# All lists will be references to other DB Objects
class Subreddit(Document):
    name = StringField(required=True)
    moderators = ListField(required=True)

    def update_sr_object(self, new_mod):
        if not (new_mod in self.moderators):
            self.moderators.append(new_mod)
        return
