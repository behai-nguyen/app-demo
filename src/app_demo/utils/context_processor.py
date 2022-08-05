"""
Template functions.
"""
from datetime import datetime
from flask import current_app as app

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