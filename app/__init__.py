# app/__init__.py

import os
import logging
from flask import Flask


# Initialize Flask application
app = Flask(__name__)



# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
handler = logging.FileHandler('app.log')  # Log to a file
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


# Propagate the logging settings to all loggers
logging.getLogger().setLevel(logging.INFO)
logging.getLogger().setLevel(logging.DEBUG)
logging.getLogger().addHandler(handler)

# Initialize BackgroundScheduler and Docker client
from apscheduler.schedulers.background import BackgroundScheduler
import docker
scheduler = BackgroundScheduler()
client = docker.from_env()




# Import routes
from app import routes




