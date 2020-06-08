import json


def aggregate_and_format_reddit_data(initial_list, dict_fields):
    # ! Make sure that you do something about reported items with Markdown Lists and lots of HTML
    formatted_list = []
    for post in initial_list:
        to_dict = vars(post)
        sub_dict = {field: to_dict[field] for field in dict_fields}
        # This is a reddit object, we want to just capture the name in it
        # May want to format that in the future
        # You can get their comment karma and stuff - worth it
        sub_dict["author"] = str(post.author)
        # Comments and Submissions have a mix of same and different keys
        # This will make sure they play nicely together
        # I would like to make something work to create a "name" for each post user_id?
        if "title" in to_dict:
            sub_dict["title"] = post.title
        elif "link_author" in to_dict:
            sub_dict["link_author"] = post.link_author
        else:
            sub_dict["body"] = post.body
        # Then it will add
        formatted_list.append(sub_dict)

    return formatted_list


def get_reported_data(sub, dict_fields):
    reported_list = []
    # format and append all reported comments
    reported_list.extend(aggregate_and_format_reddit_data(
        sub.mod.reports("comments"), dict_fields))
    # format and append all reported submissions
    reported_list.extend(aggregate_and_format_reddit_data(
        sub.mod.reports("submissions"), dict_fields))

    with open("reported.json", "w") as json_file:
        json.dump(reported_list, json_file)
