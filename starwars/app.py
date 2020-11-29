from flask import Flask
import logging
from starwars.rest import starship
from starwars.flask_settings import ProdConfig

logging.basicConfig(level=logging.INFO,
                    format='(%(threadName)-9s) %(message)s', )


def create_app(config_object=ProdConfig):
    app = Flask(__name__)
    app.config.from_object(config_object)
    app.register_blueprint(starship.blueprint)
    return app
