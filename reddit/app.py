import json
import pprint
from reddit.helpers import get_reported_data, check_users_and_add_reports
from reddit.config import subreddit


def collect_recently_reported_users():
    # Pop into the subreddit, grab actively reported posts, and store them in JSON
    # TODO This becomes the response from the database

    reported_users = []
    curr_reports = get_reported_data(subreddit)
    check_users_and_add_reports(curr_reports, reported_users)
    return reported_users
