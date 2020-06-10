import datetime
from database.models import Reported_Users

from reddit.config import subreddit


def get_reported_data(sub):
    # Shove active reports into list
    reported_list = []
    reported_list.extend(sub.mod.reports("comments"))
    reported_list.extend(sub.mod.reports("submissions"))
    # Return the full list of active reports
    return reported_list


def create_and_store_new_user(reported_item):
    reported_items_list = [reported_item.id]
    new_user_object = {
        "redditor_id": str(reported_item.author.id),
        "name": reported_item.author.name,
        "modified": datetime.datetime.now(),
        "reported_items": reported_items_list
    }
    Reported_Users(**new_user_object).save()


def add_reported_item(user, item):
    prev_reported = user.reported_items
    # If element is not found in user reported_items list
    if not any(prev_item == item.id for prev_item in prev_reported):
        print("Item not in list", item.id)
        prev_reported.append(item.id)
        user_update_object = {
            "modified": datetime.datetime.now(),
            "reported_items": prev_reported
        }
        user.update(**user_update_object)
    else:
        indexOf = prev_reported.index(item.id)
        print("Item in list", item.id, indexOf)


def check_for_repeat_offenders(reports_list):
    for item in reports_list:
        name = item.author.name
        try:
            # IF user is found, update user with new item
            found = Reported_Users.objects.get(name=name)
            add_reported_item(found, item)
        except Reported_Users.DoesNotExist:
            create_and_store_new_user(item)


def collect_recent_reports():
    print("Starting reports grab")
    recent_reports = get_reported_data(subreddit)
    if (len(recent_reports) > 0):
        print("Checking for repeat users")
        check_for_repeat_offenders(recent_reports)
    else:
        print("No new reports. Closing.")
        # Slack bot no reports
        return
