"""Flask app config settings."""
import os

class Config:
    """Set Flask configuration from .env file."""

    # General Config
    SECRET_KEY = os.getenv( 'SECRET_KEY' )
    FLASK_APP = os.getenv( 'FLASK_APP' )
    FLASK_ENV = os.getenv( 'FLASK_ENV' )

def get_config():
    """Retrieve environment configuration settings."""
    return Config