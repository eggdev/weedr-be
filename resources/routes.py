from resources.users import UsersApi, UserApi


def initialize_routes(api):
    api.add_resource(UsersApi, '/users')
    api.add_resource(UserApi, '/users/<name>')
