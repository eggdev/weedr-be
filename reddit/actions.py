import json
import pprint

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
    new_user_object = {
        "name": reported_item.author.name,
    }
    Reported_Users(**new_user_object).save()


def add_reported_item(user, item):
    user_update_object = {
        "name": item.author.name,
        "reported_items": [item]
    }
    user.update(**user_update_object)


def check_for_repeat_offenders(reports_list):
    for item in reports_list:
        name = item.author.name
        try:
            found = Reported_Users.objects.get(name=name)
            print("Found this user", name)
            # add_reported_item(found, item)
            # IF user is found, update user with new item
        except Reported_Users.DoesNotExist:
            create_and_store_new_user(item)

        # Get users in db
        # create_and_store_new_user(item)

        # If the author of this item does not exist in reported_users
        # if !(reported_users.reduce((usr) => usr.id === item.author.id));
        # if not any(usr.name == item.author.name for usr in db_users):
        #     # Instantiate new user
        #     new_reported_user = Reported_User(item.author)
        #     new_reported_user.add_reported_item(item)
        #     # And add them to this list of reported users
        #     Reported_Users(new_reported_user).save()
        # else:
        #     # pysthcript - like spanglish
        #     # found = [for (users in list) if (usr.id == author.id) return usr]
        #     found_user = [
        #         usr for usr in reported_users if usr.id == item.author.id
        #     ][0]
        #     # TODO PUT method on individual user
        #     found_user.add_reported_item(item)


def collect_recent_reports():
    print("Starting reports grab")
    recent_reports = get_reported_data(subreddit)
    if (len(recent_reports) > 0):
        print("Checking for repeat users")
        check_for_repeat_offenders(recent_reports)
    else:
        print("No reports. Closing.")
        # Slack bot no reports
        return


# def collect_recently_reported_users():
#     # Pop into the subreddit, grab actively reported posts, and store them in JSON
#     # TODO This becomes the response from the database

#     reported_users = []
#     curr_reports = get_reported_data(subreddit)
#     check_users_and_add_reports(curr_reports, reported_users)
#     return reported_users
