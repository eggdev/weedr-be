import praw
from flask import jsonify
import datetime
from database.User.models import User
from database.Subreddit.models import Subreddit
from database.Redditor.models import Redditor
from reddit.config import generate_praw_instance


def get_reported_data(sub, reddit):
    # Shove active reports into list
    sr = sub.display_name
    comments = sub.mod.reports("comment")
    submissions = sub.mod.reports("submission")
    subreddit = None
    try:
        subreddit = Subreddit.objects.get(sr=sr)
    except Subreddit.DoesNotExist:
        subreddit = Subreddit(sr=sr)
        subreddit.save()

    subreddit.add_reported_item(comments, "comment")
    subreddit.add_reported_item(submissions, "submission")
    subreddit.save()
    check_for_repeat_offenders(comments, reddit, "comment")
    check_for_repeat_offenders(submissions, reddit, "submission")


def check_for_repeat_offenders(reports_list, reddit, item_type):
    for item in reports_list:
        post = reddit.comment(
            id=item.id
        ) if item_type == "comment" else reddit.submission(
            id=item.id
        )
        username = post.author.name
        # This attribute is localized to comments as they are children of submissions
        try:
            found = Redditor.objects.get(username=username)
            found.add_reported_item(post, item_type)
        except Redditor.DoesNotExist:
            redditor = Redditor(username=username)
            redditor.add_reported_item(post, item_type)


def main():
    # Go through all users
    for user in User.objects():
        acc = user.reddit_accounts[0]
        reddit = generate_praw_instance(acc["refresh_token"])
        moderated = reddit.redditor(acc["username"]).moderated()
        for subreddit in moderated:
            get_reported_data(subreddit, reddit)
