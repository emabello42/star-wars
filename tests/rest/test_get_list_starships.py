import json
from unittest import mock
from starwars.domain.starship import Starship
import starwars.response_objects as res
import logging

starship_dict = {
    'code': "5ec280b1-e19a-4905-af40-aa3bdb292ccb",
    'name': "Y-wing",
    'hyperdrive_rating': 1.0
}

starship1 = Starship.from_dict(starship_dict)
starships = [starship1]


@mock.patch('starwars.use_cases.list_starships.ListStarshipUseCase')
def test_get(mock_use_case, client):
    mock_use_case().execute.return_value = res.ResponseSuccess(starships)
    http_response = client.get('/starships')
    assert json.loads(http_response.data.decode('UTF-8')) == [starship_dict]
    mock_use_case().execute.assert_called()
    args, kwargs = mock_use_case().execute.call_args
    assert args[0].params == {}

    assert http_response.status_code == 200
    assert http_response.mimetype == "application/json"