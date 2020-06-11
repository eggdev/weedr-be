from api.Moderator.resources import CreateModerator, LoginModerator, GetModerator


def initialize_routes(api):
    api.add_resource(CreateModerator, '/v1/signup')
    api.add_resource(LoginModerator, '/v1/login')
    api.add_resource(GetModerator, '/v1/api/m/<username>')
