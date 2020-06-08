import pandas as pd
import datetime as dt
import json
import pprint
from formatting.helpers import get_reported_data
from formatting.config import dict_fields, subreddit

# Pop into the subreddit, grab actively reported posts, and store them in JSON
get_reported_data(subreddit, dict_fields)

# Now that data is written, you need to use that data to create a user object

# This user object will track:
# Date of report
# Total # of reports on post (user && mod)
# Report type count (spam, shitpost, etc)
#


# At karma and report number threshold we will analyze karma and reports
# Will determine the suitability of their post content
