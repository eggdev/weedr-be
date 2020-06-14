import datetime
from database.db import db
from flask_bcrypt import generate_password_hash, check_password_hash
from mongoengine import Document, StringField, ListField


class User(Document):
    username = StringField(required=True)
    password = StringField(required=True)
    reddit_accounts = ListField(required=False)

    def hash_password(self):
        self.password = generate_password_hash(self.password).decode("utf8")

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def generate_return_object(self):
        return {
            "username": self.username,
            "reddit_accounts": self.reddit_accounts,
        }
