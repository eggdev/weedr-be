import praw
from flask import jsonify
import datetime
from database.User.models import User
from database.Subreddit.models import Subreddit
from database.Redditor.models import Redditor
from reddit.config import generate_praw_instance


def get_reported_data(sub):
    # Shove active reports into list
    try:
        print(sub)
    except Subreddit.DoesNotExist:
        print(sub)
    return []
    # reported_list = []
    # for comm in sub.mod.reports("comments"):
    #     reported_list.append(
    #         {"id": comm.id, "item_type": "comment"}
    #     )

    # for subm in sub.mod.reports("submissions"):
    #     reported_list.append(
    #         {"id": subm.id, "item_type": "submission"}
    #     )

    # return reported_list


def check_for_repeat_offenders(reports_list, reddit):
    for item in reports_list:
        item_type = item["item_type"]
        item_id = item["id"]
        post = reddit.comment(
            id=item_id
        ) if item_type == "comment" else reddit.submission(
            id=item_id
        )
        username = post.author.name
        # This attribute is localized to comments as they are children of submissions
        try:
            found = Redditor.objects.get(username=username)
            found.add_reported_item(post, item_type)
        except Redditor.DoesNotExist:
            redditor = Redditor(username=username)
            redditor.add_reported_item(post, item_type)


def collect_recent_reports(reddit, subreddit):
    recent_reports = get_reported_data(subreddit)
    if (len(recent_reports) > 0):
        check_for_repeat_offenders(recent_reports, reddit)


def main():
    # Go through all users
    for user in User.objects():
        acc = user.reddit_accounts[0]
        reddit = generate_praw_instance(acc["refresh_token"])
        moderated = reddit.redditor(acc["username"]).moderated()
        for subreddit in moderated:
            collect_recent_reports(reddit, subreddit)
