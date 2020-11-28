import os
import tempfile
# import yaml
import pytest
from starwars.app import create_app
from starwars.flask_settings import TestConfig

@pytest.yield_fixture(scope='function')
def app():
    return create_app(TestConfig)