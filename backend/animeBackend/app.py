# -*- coding: utf-8 -*-
"""The app module, containing the app factory function."""
from flask import Flask
from animeBackend.extensions import cors

from animeBackend import api
from animeBackend.settings import ProdConfig


def create_app(config_object=ProdConfig):
    """An application factory, as explained here:
    http://flask.pocoo.org/docs/patterns/appfactories/.

    :param config_object: The configuration object to use.
    """
    app = Flask(__name__.split('.')[0])
    app.url_map.strict_slashes = False
    app.config.from_object(config_object)
    register_blueprints(app)
    return app


def register_blueprints(app):
    """Register Flask blueprints."""
    origins = app.config.get('CORS_ORIGIN_WHITELIST', '*')
    cors.init_app(api.views.blueprint, origins=origins)

    app.register_blueprint(api.views.blueprint)

