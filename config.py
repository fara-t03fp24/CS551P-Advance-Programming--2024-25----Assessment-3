import os
from pathlib import Path

# Get folder where this file is - using pathlib because it works on all computers
basedir = Path(__file__).parent

class Config:
    """Main settings that work for all situations.
    
    All other config classes inherit from this one so we don't have to
    repeat the same settings everywhere.
    """
    # Secret key for security - should be secret in production!
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-key-1234'
    
    # Database location - using SQLite because it's easy to set up
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        f'sqlite:///{basedir}/cybersecurity_events.db'
    
    # Turn off SQLAlchemy's event system - we don't need it
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class TestConfig(Config):
    """Settings for running tests.
    
    Uses a temporary database in memory - makes tests run super fast
    and doesn't mess with our real data!
    """
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'

class DevelopmentConfig(Config):
    """Settings for when I'm developing the app.
    
    Debug mode on = shows error details and reloads when code changes.
    Really helpful while building the app!
    """
    DEBUG = True

class ProductionConfig(Config):
    """Settings for the live app on Render.
    
    Debug mode off for security + better performance.
    """
    DEBUG = False

# Dictionary to pick which config to use
# Default = development settings for easier coding
config = {
    'development': DevelopmentConfig,
    'testing': TestConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}