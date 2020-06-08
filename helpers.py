def aggregate_and_format_reddit_data(initial_list, dict_fields):
    # ! Make sure that you do something about reported items with Markdown Lists and lots of HTML
    formatted_list = []
    for post in initial_list:
        to_dict = vars(post)
        sub_dict = {field: to_dict[field] for field in dict_fields}
        sub_dict["author"] = str(post.author)
        if "title" in to_dict:
            sub_dict["title"] = post.title
        elif "link_author" in to_dict:
            sub_dict["link_author"] = post.link_author
        else:
            sub_dict["body"] = post.body

        formatted_list.append(sub_dict)
    return formatted_list
