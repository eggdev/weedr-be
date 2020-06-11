from api.Moderator.resources import CreateModerator


def initialize_routes(api):
    api.add_resource(CreateModerator, '/v1/auth')
