from flask import jsonify
import datetime
from database.models import Reported_Users, Reported_Item

from reddit.config import subreddit


def get_reported_data(sub):
    # Shove active reports into list
    reported_list = []
    reported_list.extend(sub.mod.reports("comments"))
    reported_list.extend(sub.mod.reports("submissions"))
    # Return the full list of active reports
    return reported_list


def create_and_store_new_user(reported_item, item_type):
    first_reported_item = {"item_id": reported_item.id, "item_type": item_type}

    new_user_object = {
        "user_id": reported_item.author.id,
        "name": reported_item.author.name,
        "modified": datetime.datetime.now(),
        "reported_items": [Reported_Item(**first_reported_item)],
    }
    Reported_Users(**new_user_object).save()


def add_reported_item(user, item, item_type):
    prev_reported = user.reported_items
    # If element is not found in user reported_items list

    print(prev_reported)
    if not any(prev_item["item_id"] == item.id for prev_item in prev_reported):
        newly_reported_item = {"item_id": item.id, "item_type": item_type}
        readied = Reported_Item(**newly_reported_item)
        prev_reported.append(readied)

        user_update_object = {
            "modified": datetime.datetime.now(),
            "reported_items": prev_reported
        }
        user.update(**user_update_object)
    else:
        return


def check_for_repeat_offenders(reports_list):
    for item in reports_list:
        name = item.author.name
        # This attribute is localized to comments as they are children of submissions
        reported_item_type = "comments" if hasattr(
            item, "submission") else "submissions"
        found = len(Reported_Users.objects(name=name)) > 0
        if found:
            # If user is found, update user with new item
            add_reported_item(Reported_Users.objects.get(
                name=name), item, reported_item_type)
        else:
            create_and_store_new_user(
                item,  reported_item_type)


def collect_recent_reports():
    print('starting')
    recent_reports = get_reported_data(subreddit)
    if (len(recent_reports) > 0):
        check_for_repeat_offenders(recent_reports)
    else:
        print("No new reports. Closing.")
        # Slack bot no reports
        return
