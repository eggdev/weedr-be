from flask import jsonify
import datetime
from database.models import Reported_Users, Reported_Item

from reddit.config import subreddit


def generate_report_item(item):
    item_type = "comment" if hasattr(
        item, "submission") else "submission"
    prepped = {"item_id": item.id, "item_type": item_type}
    return Reported_Item(**prepped)


def get_reported_data(sub):
    # Shove active reports into list
    reported_list = []
    reported_list.extend(sub.mod.reports("comments"))
    reported_list.extend(sub.mod.reports("submissions"))
    # Return the full list of active reports
    return reported_list


def create_and_store_new_user(reported_item):
    first_reported_item = generate_report_item(reported_item)
    new_user_object = {
        "user_id": reported_item.author.id,
        "name": reported_item.author.name,
        "modified": datetime.datetime.now(),
        "reported_items": [first_reported_item],
    }
    Reported_Users(**new_user_object).save()


def add_reported_item(user, item):
    prev_reported = user.reported_items
    # If element is not found in user reported_items list
    if not any(prev_item["item_id"] == item.id for prev_item in prev_reported):
        newly_reported_item = generate_report_item(item)
        prev_reported.append(newly_reported_item)

        user_update_object = {
            "modified": datetime.datetime.now(),
            "reported_items": prev_reported
        }
        user.update(**user_update_object)
    else:
        # Gonna need to find the report in their object, and update it with the latest version of itself
        return


def check_for_repeat_offenders(reports_list):
    for item in reports_list:
        name = item.author.name
        # This attribute is localized to comments as they are children of submissions
        found = len(Reported_Users.objects(name=name)) > 0
        if found:
            # If user is found, update user with new item
            add_reported_item(Reported_Users.objects.get(name=name), item)
        else:
            create_and_store_new_user(item)


def collect_recent_reports():
    print('starting')
    recent_reports = get_reported_data(subreddit)
    if (len(recent_reports) > 0):
        check_for_repeat_offenders(recent_reports)
    else:
        print("No new reports. Closing.")
        # Slack bot no reports
        return
