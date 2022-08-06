"""
The echo Blueprint handles POST and GET requests to /echo route.
"""
from flask import Blueprint

echo_blueprint = Blueprint( 'echo', __name__, template_folder='templates' )
