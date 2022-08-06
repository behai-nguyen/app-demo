"""
Application routes functional tests.
"""
import pytest

@pytest.mark.hello_world
def test_hello_world( test_client ):
    """
    Test '/' route.
    """
    response = test_client.get( '/' )
    assert response.status_code == 200
    assert b'Hello, World!' in response.data
    assert 'Hello, World!' in response.data.decode( 'utf-8' )

@pytest.mark.echo
def test_echo_get_1( test_client ):
    """
    Test '/echo' route with GET: no trailing back slash.
    """
    response = test_client.get( '/echo' )

    html = response.data.decode( 'utf-8' )

    assert '<h1>Method: GET</h1>' in html

    assert '<h1>Blueprint: echo</h1>' in html
    assert '<h1>Endpoint: do_echo</h1>' in html

@pytest.mark.echo
def test_echo_get_2( test_client ):
    """
    Test '/echo/' route with GET: with trailing back slash.
    """
    response = test_client.get( '/echo/' )

    html = response.data.decode( 'utf-8' )

    assert '<h1>Method: GET</h1>' in html

    assert '<h1>Blueprint: echo</h1>' in html
    assert '<h1>Endpoint: do_echo</h1>' in html

@pytest.mark.echo
def test_echo_post( test_client ):
    """
    Test '/echo' route with POST.
    """
    response = test_client.post(
        '/echo',
        data={ 'name1': 'Nguyen', 'name2': 'Van Be Hai', 'dob': '6/7/1800' }
    )

    html = response.data.decode( 'utf-8' )

    assert '<h1>Method: POST</h1>' in html

    assert '<h1>Blueprint: echo</h1>' in html
    assert '<h1>Endpoint: do_echo</h1>' in html

    assert '<h3>Key: name1. Value: Nguyen</h3>' in html
    assert '<h3>Key: name2. Value: Van Be Hai</h3>' in html
    assert '<h3>Key: dob. Value: 6/7/1800</h3>' in html