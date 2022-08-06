"""Flask app initialization via factory pattern."""
from flask import Flask

from app_demo.config import get_config
from app_demo.utils.functions import template_root_path

def create_app():
    app = Flask( 'dsm-python-demo', template_folder=template_root_path() )

    app.config.from_object( get_config() )

    app.url_map.strict_slashes = False

    @app.route( '/' )
    def hello_world():
        return '<p>Hello, World!</p>'

    register_blueprints( app )

    return app

def register_blueprints( app ):
    """
    Register blueprints	and routes.
    """
    from app_demo import urls

    for url in urls.urls:
        url[ 2 ].add_url_rule( url[0], methods=url[1], view_func=url[3] )

    for blueprint in urls.blueprints:
        app.register_blueprint( blueprint )