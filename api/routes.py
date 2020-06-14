from api.User.resources import Signup, Login, Logout, UserAccount


def initialize_routes(api):
    api.add_resource(Signup, '/v1/signup')
    api.add_resource(Login, '/v1/login')
    api.add_resource(Logout, '/v1/logout')
    api.add_resource(UserAccount, '/v1/api/self')
