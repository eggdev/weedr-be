from api.User.resources import Signup, Login, Logout, UserAccount, RedditAuth
from api.Subreddit.resources import SubredditRequests


def initialize_routes(api):
    api.add_resource(Signup, '/v1/signup')
    api.add_resource(Login, '/v1/login')
    api.add_resource(Logout, '/v1/logout')
    api.add_resource(UserAccount, '/v1/api/self')
    api.add_resource(RedditAuth, '/v1/api/auth')
    api.add_resource(SubredditRequests, '/v1/api/r/<subreddit>')
