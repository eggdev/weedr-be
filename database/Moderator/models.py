import datetime
from database.db import db
from flask_bcrypt import generate_password_hash, check_password_hash
from mongoengine import Document, StringField, ListField
from database.Subreddit.models import Subreddit


class Moderator(Document):
    username = StringField(required=True)
    password = StringField(required=True)
    subreddits = ListField(required=True)

    def hash_password(self):
        self.password = generate_password_hash(self.password).decode("utf8")

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def generate_return_object(self):
        return {
            "username": self.username,
            "subreddits": self.subreddits,
        }

    def generate_moderated_subreddits(self, reddit):
        # Will check for all subreddits a user moderates and add them to the object
        moderated_subreddits = reddit.get(
            f"/user/{self.username}/moderated_subreddits")
        if "data" in moderated_subreddits:
            for sub in moderated_subreddits["data"]:
                # Generate new Subreddit in Database
                try:
                    sr = Subreddit.objects.get(name=sub["sr"])
                    sr.update_sr_object(self.username)
                    sr.save()
                except Subreddit.DoesNotExist:
                    new_subreddit = Subreddit(name=sub["sr"])
                    new_subreddit.update_sr_object(self.username)
                    new_subreddit.save()
                self.subreddits.append(sub["sr"])
        return
