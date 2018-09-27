from typing import Optional

from flask import Flask
from openbrokerapi.api import BrokerCredentials

from .broker import Broker


def create_app(credentials: Optional[BrokerCredentials] = None):
    app = Flask(__name__)

    app.register_blueprint(broker.create_broker_blueprint(credentials))

    # Endpoint to test if server comes up
    @app.route('/ping')
    def ping():
        return 'PONG'

    return app
