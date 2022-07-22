"""Flask app initialization via factory pattern."""
from flask import Flask

from app_demo.config import get_config

def create_app():
    app = Flask( 'dsm-python-demo' )

    app.config.from_object( get_config() )

    @app.route( '/' )
    def hello_world():
        return '<p>Hello, World!</p>'

    return app