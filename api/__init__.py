from flask import Flask
from flask_migrate import Migrate

from api.adapters import database as db
from api.application import controllers

migrate = Migrate()


def create_app(test_config=None):
    app = Flask(__name__)

    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(test_config)

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(controllers.user_blueprint)

    return app
