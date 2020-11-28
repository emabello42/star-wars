from flask import Flask
import logging
from starwars.rest import starship
from starwars.flask_settings import DevConfig

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s', )

def create_app(config_object=DevConfig):
    app = Flask(__name__)
    app.config.from_object(config_object)
    app.register_blueprint(starship.blueprint)
    return app
