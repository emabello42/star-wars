import starwars.response_objects as res


class ListStarshipUseCase:
    def __init__(self, repo):
        self.repo = repo

    def execute(self, req_obj):
        if not req_obj:
            return res.ResponseFailure.build_from_invalid_request_object(req_obj)
        try:
            starships = self.repo.list_starships()
            return res.ResponseSuccess(starships)
        except Exception as exc:
            return res.ResponseFailure.build_system_error("{}: {}".format(exc.__class__.__name__, "{}".format(exc)))