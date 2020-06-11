import praw
import json
from reddit.config import reddit


def format_user_object(user):
    praw_user = reddit.redditor(name=user.name)
    formatted_reported_items = []
    for item in user.reported_items:
        itemdata = ""
        if item.item_type == "comment":
            itemdata = reddit.comment(id=item.item_id)
        elif item.item_type == "submission":
            itemdata = reddit.submission(id=item.item_id)

        formatted_reported_items.append({
            "item_id": item.item_id,
            "item_type": item.item_type,
            "mod_reports": itemdata.mod_reports,
            "user_reports": itemdata.user_reports,
        })
    return json.dumps({
        "name": praw_user.name,
        "comment_karma": praw_user.comment_karma,
        "link_karma": praw_user.link_karma,
        "reported_items": formatted_reported_items,
    })
