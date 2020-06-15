import datetime
import praw
import requests
import json
from database.db import db
from flask_bcrypt import generate_password_hash, check_password_hash
from mongoengine import Document, StringField, ListField
from reddit.config import generate_praw_instance


class User(Document):
    username = StringField(required=True)
    password = StringField(required=True)
    reddit_accounts = ListField(required=False)

    def hash_password(self):
        self.password = generate_password_hash(self.password).decode("utf8")

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def add_account(self, username, refresh_token):
        self.reddit_accounts.append(
            {"username": username, "refresh_token": refresh_token}
        )
        return self.reddit_accounts

    def update_refresh_token(self):
        acc = self.reddit_accounts[0]
        token = acc["refresh_token"]
        return generate_praw_instance(token)

    def generate_return_object(self):
        return {
            "username": self.username,
            "reddit_accounts": self.reddit_accounts,
        }
