import time
from multiprocessing import Process
from unittest import TestCase

import requests


class ServerTest(TestCase):
    def setUp(self):
        def run_server():
            from broker import create_app
            create_app().run()

        self.server = Process(target=run_server)
        self.server.start()
        time.sleep(0.5)

    def test_returns_pong(self):
        response = requests.get("http://localhost:5000/ping")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, 'PONG')

    def tearDown(self):
        self.server.terminate()
        self.server.join()
