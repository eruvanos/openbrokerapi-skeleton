import logging
import os

from flask import Flask
from openbrokerapi.api import BrokerCredentials

from . import log_util

# Configure logging
log_util.configure(logging.root, log_level='INFO')
logger = logging.getLogger(__name__)


def start_app(app: Flask, port: int):
    from waitress import serve
    serve(app, host='0.0.0.0', port=port)


def main():
    from . import create_app

    # Read config from env
    broker_username = os.getenv('BROKER_USERNAME')
    broker_password = os.getenv('BROKER_PASSWORD')

    # Setup auth if env vars are set
    if broker_username and broker_password:
        credentials = BrokerCredentials(broker_username, broker_password)
    else:
        credentials = None

    start_app(
        app=create_app(credentials),
        port=int(os.getenv('PORT', '5000')),
    )


if __name__ == '__main__':
    main()
