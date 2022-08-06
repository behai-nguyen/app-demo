"""pytest entry. To run all tests:

1. venv\\Scripts\\python.exe -m pytest
2. venv\\Scripts\\pytest.exe

To run individual tests:

venv\\Scripts\\pytest.exe -m <@pytest.mark>

Valid @pytest.marks are defined in pytest.ini.
"""
import pytest

from app_demo import create_app

@pytest.fixture(scope='module')
def app():
    """
    Application fixure.	
    """
    app = create_app()
	
    app.app_context().push()
    """
    Making all custom template functions available 
	to the test application instance.
    """	
    from app_demo.utils import context_processor

    return app

@pytest.fixture(scope='module')
def test_client( app ):
    """
    Creates a test client.
	app.test_client() is able to submit HTTP requests.

    The app argument is the app() fixure above.	
    """
    with app.test_client() as testing_client:
        yield testing_client  # Return to caller.