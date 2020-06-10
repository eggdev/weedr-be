from resources.users import ManyUsersApi, SingleUserApi


def initialize_routes(api):
    api.add_resource(ManyUsersApi, '/users')
    api.add_resource(SingleUserApi, '/users/<name>')
