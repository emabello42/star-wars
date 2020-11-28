import starwars.response_objects as res

class ListStarshipUseCase:
    def __init__(self, repo):
        self.repo = repo
        self.default_params = {'orderby_hyperdrive_asc'}

    def execute(self, req_obj):
        if not req_obj:
            return res.ResponseFailure.build_from_invalid_request_object(req_obj)

        try:
            params = req_obj.params if req_obj.params else self.default_params
            starships = self.repo.list_starships(params=params)
            return res.ResponseSuccess(starships)
        except Exception as exc:
            return res.ResponseFailure.build_system_error("{}: {}".format(exc.__class__.__name__, "{}".format(exc)))