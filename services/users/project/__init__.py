import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_debugtoolbar import DebugToolbarExtension
from flask_cors import CORS


# Instantiate the DB
db = SQLAlchemy()
# Instatiate the extension
toolbar = DebugToolbarExtension()
cors = CORS()


def create_app(script_info=None):
    # Instatiate the app
    app = Flask(__name__)

    # Set config
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    # set up extensions
    db.init_app(app)
    toolbar.init_app(app)  
    cors.init_app(app)  

    # register blueprints
    from project.api.users import users_blueprint
    app.register_blueprint(users_blueprint)

    # shell context for flask cli
    @app.shell_context_processor
    def ctx():
        return {'app': app, 'db': db}

    return app
