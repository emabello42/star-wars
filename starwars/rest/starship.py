import json
from flask import Blueprint, request, Response

from starwars.repository.postgresrepo import PostgresRepo
import starwars.use_cases.list_starships as uc
from starwars.serializers import StartshipJsonEncoder
import starwars.response_objects as res
import starwars.request_objects as req

blueprint = Blueprint('starship', __name__)

STATUS_CODES = {
    res.ResponseSuccess.SUCCESS: 200,
    res.ResponseFailure.SYSTEM_ERROR: 500
}

connection_data = {
    'dbname': "starwarsdb",
    'user': "postgres",
    'password': "",
    'host': "localhost"
}


@blueprint.route('/starships', methods=['GET'])
def starship():
    query_params = {
        'params': {}
    }
    for arg, values in request.args.items():
        if arg.startswith('param_'):
            query_params['params'][arg.replace('param_', '')] = values
    req_obj = req.StarshipRequestObject.from_dict(query_params)
    repo = PostgresRepo(connection_data)
    use_case = uc.ListStarshipUseCase(repo)
    response = use_case.execute(req_obj)
    return Response(json.dumps(response.value, cls=StartshipJsonEncoder),
                    mimetype='application/json',
                    status=STATUS_CODES[response.type])
