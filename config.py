# config.py

import logging
import os

class Config:
    """
    Base configuration class.
    """
    UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'scripts')
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get('SECRET_KEY', 'default-secret-key')
    PORT = int(os.environ.get('PORT', 5000))
    # Add other configuration options as needed

class DevelopmentConfig(Config):
    """
    Development configuration class.
    """
    DEBUG = True
    # Add development-specific configuration options if needed

class ProductionConfig(Config):
    """
    Production configuration class.
    """
    # Add production-specific configuration options if needed
    pass

class TestingConfig(Config):
    """
    Testing configuration class.
    """
    TESTING = True
    UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'test_scripts')
    # Add testing-specific configuration options if needed

# Dictionary to hold the different configuration classes
config_dict = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}

# Select the configuration class based on the environment 
def get_config(env):
    try:
        return config_dict.get(env, Config)()
    except Exception as e:
        logging.exception('An error occurred while getting configuration: %s', e)
        return Config()

