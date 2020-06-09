class User(object):
    def __init__(self, redditor):
        self.id = redditor.id
        self.comment_karma = redditor.comment_karma
        self.link_karma = redditor.link_karma
        self.is_mod = redditor.is_mod
        self.name = redditor.name
        self.reported_items = []

    def add_reported_item(self, item):
        # if !(reported_users.reduce((usr) => usr.id === item.author.id));
        # If the passed item does not exist in the users already reported list
        if not any(already_reported.id == item.id for already_reported in self.reported_items):
            self.reported_items.append(item)
