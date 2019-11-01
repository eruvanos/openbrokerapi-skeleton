import logging
import os
from typing import Optional

from flask import Flask
from openbrokerapi.api import BrokerCredentials

from . import log_util
from .broker import Broker

# Configure logging
# You can overwrite the log_level by setting LOG_LEVEL in the environment
log_util.configure(logging.root, log_level='INFO', )
logger = logging.getLogger(__name__)


def setup_app(credentials: Optional[BrokerCredentials] = None) -> Flask:
    app = Flask(__name__)

    app.register_blueprint(broker.create_broker_blueprint(credentials))

    # Endpoint to test if server comes up
    @app.route('/ping')
    def ping():
        return 'PONG'

    return app


def create_app():
    # Read config from env
    broker_username = os.getenv('BROKER_USERNAME')
    broker_password = os.getenv('BROKER_PASSWORD')

    # Setup auth if env vars are set
    if broker_username and broker_password:
        credentials = BrokerCredentials(broker_username, broker_password)
    else:
        credentials = None

    return setup_app(credentials)
