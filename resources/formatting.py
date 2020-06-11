import praw
import json
from reddit.config import reddit


def format_user_object(user):
    praw_user = reddit.redditor(name=user.name)
    formatted_reported_items = []
    for item in user.reported_items:
        if item.item_type == "comment":
            comment = reddit.comment(id=item.item_id)
            formatted_reported_items.append({
                "item_id": item.item_id,
                "item_type": item.item_type,
                "mod_reports": comment.mod_reports,
                "user_reports": comment.user_reports,
            })
        elif item.item_type == "submission":
            submission = reddit.submission(id=item.item_id)
            formatted_reported_items.append({
                "item_id": item.item_id,
                "item_type": item.item_type,
                "mod_reports": submission.mod_reports,
                "user_reports": submission.user_reports,
            })
    json_version = {
        "name": praw_user.name,
        "comment_karma": praw_user.comment_karma,
        "link_karma": praw_user.link_karma,
        "reported_items": formatted_reported_items,
    }
    return json.dumps(json_version)
