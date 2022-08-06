"""
Echo route.
"""
from flask import render_template

def do_echo():
    return render_template( 'echo/echo.html' )