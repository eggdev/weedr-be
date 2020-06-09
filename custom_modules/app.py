import json
import pprint
from helpers import get_reported_data, check_users_and_add_reports
from config import subreddit, reddit
from user import User

# TODO This becomes the response from the database
reported_users = []

# Pop into the subreddit, grab actively reported posts, and store them in JSON
curr_reports = get_reported_data(subreddit)
check_users_and_add_reports(curr_reports, reported_users)


for bad_guys in reported_users:
    print(bad_guys.name, bad_guys.redditor.name)

# Build out flask app

# Alright now we have users being turned into custom objects
# Those users have multiple submissions in their list of reports


# Need a place to store for users
# This user object will track:
# Build new one if it doesnt exist
# Date of report
# Total # of reports on post (user && mod)
# Report type count (spam, shitpost, etc)
# Check it's exsistence in DB (some file for now)
# When at karma and report number threshold we will analyze karma and reports
# Will determine the suitability of their post content
