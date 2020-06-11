from api.Redditor.users import ManyUsersApi, SingleUserApi

from api.Subreddit.resources import GetAllReportedItems


def initialize_routes(api):
    api.add_resource(GetAllReportedItems, '/r/<subreddit>')
