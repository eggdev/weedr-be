class User(object):
    def __init__(self, redditor):
        self.id = redditor.id
        self.name = redditor.name
        self.redditor = redditor
        self.reported_items = []
        self.reported_by_mod_count = 0
        self.reported_by_user_count = 0

    def add_reported_item(self, item):
        # if !(reported_users.reduce((usr) => usr.id === item.author.id));
        # If the passed item does not exist in the users already reported list
        if not any(prev_reported.id == item.id for prev_reported in self.reported_items):
            self.reported_items.append(item)
