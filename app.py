import pandas as pd
import datetime as dt
import json
import pprint
from formatting.helpers import aggregate_and_format_reddit_data
from formatting.config import dict_fields, subreddit, reported_list


def get_reported_data(sub):
    # format and append all reported comments
    reported_list.extend(aggregate_and_format_reddit_data(
        sub.mod.reports("comments"), dict_fields))

    # format and append all reported submissions
    reported_list.extend(aggregate_and_format_reddit_data(
        sub.mod.reports("submissions"), dict_fields))


get_reported_data(subreddit)
with open("reported.json", "w") as json_file:
    json.dump(reported_list, json_file)
