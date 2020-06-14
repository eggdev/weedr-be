import praw
from flask import jsonify
import datetime
from database.User.models import User, CLIENT_ID, CLIENT_SECRET, USER_AGENT


def generate_report_item(item):
    # item_type = "comment" if hasattr(
    #     item, "submission") else "submission"
    # prepped = {"item_id": item.id, "item_type": item_type}
    # return Reported_Item(**prepped)
    return


def get_reported_data(sub):
    # Shove active reports into list
    reported_list = []
    reported_list.extend(sub.mod.reports("comments"))
    reported_list.extend(sub.mod.reports("submissions"))
    # Return the full list of active reports
    return reported_list


def create_and_store_new_user(reported_item):
    return
    # first_reported_item = generate_report_item(reported_item)
    # new_user_object = {
    #     "user_id": reported_item.author.id,
    #     "name": reported_item.author.name,
    #     "modified": datetime.datetime.now(),
    #     "reported_items": [first_reported_item],
    # }
    # Reported_Users(**new_user_object).save()


def add_reported_item(user, item):
    # prev_reported = user.reported_items
    # # If element is not found in user reported_items list
    # if not any(prev_item["item_id"] == item.id for prev_item in prev_reported):
    #     newly_reported_item = generate_report_item(item)
    #     prev_reported.append(newly_reported_item)

    #     user_update_object = {
    #         "modified": datetime.datetime.now(),
    #         "reported_items": prev_reported
    #     }
    #     user.update(**user_update_object)
    # else:
    #     # Gonna need to find the report in their object, and update it with the latest version of itself
    #     return
    return


def check_for_repeat_offenders(reports_list):
    for item in reports_list:
        name = item.author.name
        # This attribute is localized to comments as they are children of submissions
        # found = len(Reported_Users.objects(name=name)) > 0
        found = False
        if found:
            # If user is found, update user with new item
            # add_reported_item(Reported_Users.objects.get(name=name), item)
            return
        else:
            # create_and_store_new_user(item)
            return


def collect_recent_reports(subreddit):
    recent_reports = get_reported_data(subreddit)

    if (len(recent_reports) > 0):
        check_for_repeat_offenders(recent_reports)


def main():
    for user in User.objects():
        acc = user.reddit_accounts[0]
        reddit = praw.Reddit(
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            refresh_token=acc["refresh_token"],
            user_agent=USER_AGENT
        )

        moderated = reddit.redditor(acc["username"]).moderated()
        for subreddit in moderated:
            collect_recent_reports(subreddit)
