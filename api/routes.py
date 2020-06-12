from api.Moderator.resources import CreateModerator, LoginModerator, LogoutModerator, GetModerator


def initialize_routes(api):
    api.add_resource(CreateModerator, '/v1/signup')
    api.add_resource(LoginModerator, '/v1/login')
    api.add_resource(LogoutModerator, '/v1/logout')
    api.add_resource(GetModerator, '/v1/api/self')
