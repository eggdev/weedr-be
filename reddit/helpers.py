import json
from reddit.user import User


def get_reported_data(sub):
    """
        Params
        ------
        subreddit = The praw.Reddit.subreddit response

    """
    reported_list = []
    reported_list.extend(sub.mod.reports("comments"))
    reported_list.extend(sub.mod.reports("submissions"))

    # Return the full list of active reports
    return reported_list


def check_users_and_add_reports(curr_reports, reported_users):
    for item in curr_reports:
        # If the author of this item does not exist in reported_users
        # if !(reported_users.reduce((usr) => usr.id === item.author.id));
        if not any(usr.id == item.author.id for usr in reported_users):
            # Instantiate new user
            new_user = User(item.author)
            new_user.add_reported_item(item)
            # And add them to this list of reported users
            # TODO PUT method reported_users
            reported_users.append(new_user)
        else:
            # pysthcript - like spanglish
            # found = [for (users in list) if (usr.id == author.id) return usr]
            found_user = [
                usr for usr in reported_users if usr.id == item.author.id
            ][0]
            # TODO PUT method on individual user
            found_user.add_reported_item(item)
