# instance/config.py

import logging

# Initialize logger
logger = logging.getLogger(__name__)

try:
    # Define your instance-specific configuration variables here
    SECRET_KEY = '2f6d1c2ec5c68963b272d58e267db064'
    DATABASE_URI = 'your_database_uri'
    # Add other configuration variables as needed
except Exception as e:
    logger.exception('An error occurred while loading instance configuration: %s', e)
