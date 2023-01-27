"""
Routes mappers.
"""
from app_demo.controllers import ( 
    echo_blueprint,
    json_blueprint,
	echo,
    json_dumps,
)

"""
https://stackoverflow.com/questions/33241050/trailing-slash-triggers-404-in-flask-path-rule
Trailing slash triggers 404 in Flask path rule

url_map.strict_slashes = False 

@bp.route('/my-route', methods=['POST'])

/my-route and /my-route/ both work identically.
"""
urls = [
    ( '/echo', [ 'GET', 'POST' ], echo_blueprint, echo.do_echo ),
    ( '/json', [ 'GET' ], json_blueprint, json_dumps.do_json_dumps ),
    ( '/datetime', [ 'GET', 'POST' ], echo_blueprint, echo.echo_datetime_info ),
]

blueprints = [ echo_blueprint, json_blueprint ]