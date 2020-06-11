import praw
from json import dumps, JSONEncoder
from reddit.config import reddit

# comment = reddit.comment('em3rygg')


def format_user_object(user):
    praw_user = reddit.redditor(name=user.name)
    formatted_reported_items = []
    for item in user.reported_items:
        print("formatting", type(item))
    return {
        "name": praw_user.name,
        "comment_karma": praw_user.comment_karma,
        "link_karma": praw_user.link_karma,
        "reported_items": formatted_reported_items,
    }
