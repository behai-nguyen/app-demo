"""
Template functions.
"""
from datetime import datetime
from flask import current_app as app

import simplejson as json

@app.context_processor
def print_echo():
    def __print_echo( request ):
        """
            Arguments:

                request:
                    Flask request object.
            Return:
                { 'blueprint': [ blueprint name ], 'endpoint': [ endpoint name ],
				  'datetime': [ current datetime ],
				  <'data': [(post_key_1, post_value_1)...(post_key_n, post_value_n)]>}
        """
        tokens = request.endpoint.split( '.' )
        data = { 'blueprint': tokens[ 0 ],
            'endpoint': tokens[ 1 ],
            'datetime': datetime.now().strftime( '%d/%m/%Y, %H:%M:%S' )
        }

        if request.method == 'POST':
            data[ 'data' ] = request.form.to_dict().items()

        return data

    return dict( print_echo=__print_echo )

def json_dumps( obj: dict ):
    return json.dumps( obj )

@app.context_processor
def json_dumps_context_processor():
    def __json_dumps_context_processor( obj: dict ):
        return json_dumps( obj )

    return dict( json_dumps_context_processor=__json_dumps_context_processor )

@app.template_global()
def json_dumps_template_global( obj: dict ):
    return json_dumps( obj )

@app.template_filter()
def json_dumps_decorator_filter( obj: dict ):
    return json_dumps( obj )
	
"""
This registration gets executed automatically by the import 
statement, thereby enabling json_dumps_jinja_filter available
to template rendering function.
"""
app.jinja_env.filters[ 'json_dumps_jinja_filter' ] = json_dumps