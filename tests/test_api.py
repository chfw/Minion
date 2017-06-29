import sys
import json

from nose.tools import eq_
from minion.app import create_app


PY2 = sys.version_info[0] == 2


class TestViews:
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_api_run_view(self):
        data = {
            'command': 'ls -l'
        }
        response = self._request_api_run_view(data)
        if PY2:
            response_json = json.loads(response.data)
        else:
            response_json = json.loads(
                response.data.decode('utf-8'))
        eq_(response.status_code, 200)
        assert('setup.py' in response_json['result'])

    def test_api_run_view_with_wrong_payload(self):
        data = {
            'commando': 'ls -l'
        }
        response = self._request_api_run_view(data)
        if PY2:
            response_json = json.loads(response.data)
        else:
            response_json = json.loads(
                response.data.decode('utf-8'))
        eq_(response.status_code, 400)
        assert('In correct instructions, Master' in response_json['message'])

    def _request_api_run_view(self, data):
        headers = {
            'Content-Type': 'application/json'
        }
        response = self.client.post(
            '/api/run/',
            data=json.dumps(data),
            headers=headers)
        return response
