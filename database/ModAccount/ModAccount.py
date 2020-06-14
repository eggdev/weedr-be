import datetime
from database.db import db
from mongoengine import Document, StringField, ListField, BooleanField


class ModAccount(Document):
    username = StringField(required=True)
    refresh_token = StringField(required=True)
    is_mod = BooleanField(required=True)
    moderated_subreddits = ListField(required=True)

    def setup_mod_account(self, reddit):
        return
