import json
from config import dict_fields


def aggregate_and_format_reddit_data(initial_list):
    """
        Params
        ------
        initial_list = Either reported Submissions or Comments
    """

    # ! Make sure that you do something about reported items with Markdown Lists and lots of HTML
    formatted_list = []
    for post in initial_list:
        to_dict = vars(post)
        sub_dict = {field: to_dict[field] for field in dict_fields}
        # TODO This will need to actually just call and apply this information to the author - no json output yet
        sub_dict["author"] = str(post.author)

        # Comments and Submissions have a mix of same and different keys
        if "title" in to_dict:
            sub_dict["title"] = post.title
        elif "link_author" in to_dict:
            sub_dict["link_author"] = post.link_author
        else:
            sub_dict["body"] = post.body

        # Then it will add the json object to a list
        formatted_list.append(sub_dict)
    return formatted_list


def get_reported_data(sub):
    """
        Params
        ------
        subreddit = The praw.Reddit.subreddit response

    """
    reported_list = []
    # format and append all reported comments
    reported_list.extend(aggregate_and_format_reddit_data(
        sub.mod.reports("comments")))
    # format and append all reported submissions
    reported_list.extend(aggregate_and_format_reddit_data(
        sub.mod.reports("submissions")))

    # Returned and built lists will generate a json file
    # ** Temporary feature as a stop point
    with open("reported.json", "w") as json_file:
        json.dump(reported_list, json_file)
