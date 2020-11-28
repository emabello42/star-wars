import pytest
from starwars.domain.starship import Starship
from starwars.use_cases.list_starships import ListStarshipUseCase
from starwars.request_objects import StarshipRequestObject
import uuid
from unittest import mock


@pytest.fixture
def domain_starships():
    starship1 = Starship(code=uuid.uuid4(), name="X-wing", hyperdrive_rating=1.0)
    starship2 = Starship(code=uuid.uuid4(), name="Naboo Royal Starship", hyperdrive_rating=1.8)
    starship3 = Starship(code=uuid.uuid4(), name="B-wing", hyperdrive_rating=2.0)
    return [starship1, starship2, starship3]


def test_list_starship_orderby_hyperdrive(domain_starships):
    repo = mock.Mock()
    repo.list_starships.return_value = domain_starships
    starship_list_use_case = ListStarshipUseCase(repo)
    request = StarshipRequestObject()
    response = starship_list_use_case.execute(request)
    assert bool(response) is True
    repo.list_starships.assert_called_with(params={'orderby_hyperdrive_desc'})  # test defaults
    assert response.value == domain_starships
