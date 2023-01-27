"""
Echo route.
"""
from flask import render_template
import time

def do_echo():
    return render_template( 'echo/echo.html' )

def echo_datetime_info():
    return time.strftime("Date, Time Info: %Y-%m-%d %H:%M:%S %Z, The time offset: %z",time.localtime())
