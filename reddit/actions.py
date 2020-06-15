import praw
from flask import jsonify
import datetime
from database.User.models import User
from database.Subreddit.models import Subreddit
from database.Redditor.models import Redditor
from reddit.config import generate_refresh_praw_instance
from pprint import pprint


def check_for_repeat_offenders(reports, reddit):
    for item in reports:
        redditor = None
        try:
            redditor = Redditor.objects.get(username=item.author.name)
        except Redditor.DoesNotExist:
            redditor = Redditor(username=item.author.name)
        if item.author.name == redditor.username:
            redditor.add_reported_item(item)
            redditor.save()


def get_reported_data(sub, reddit):
    # Shove active reports into list
    sr = sub.display_name
    reported_items = sub.mod.reports()

    check_for_repeat_offenders(reported_items, reddit)
    subreddit = None
    try:
        subreddit = Subreddit.objects.get(sr=sr)
    except Subreddit.DoesNotExist:
        subreddit = Subreddit(sr=sr)
        subreddit.save()
    subreddit.add_reported_items(reported_items)
    subreddit.save()


def main():
    # Go through all users
    for user in User.objects():
        reddit = user.generate_praw_instance()
        acc = user.reddit_accounts[0]
        moderated = reddit.redditor(acc["username"]).moderated()
        for subreddit in moderated:
            get_reported_data(subreddit, reddit)
