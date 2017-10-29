import json
import requests


class Request:
    """
        Http GET, POST, PUT and DELETE requests implementation
    """

    def get(self, url, data=None, content_type='application/json'):
        return requests.get(url)

    def put(self, url, data={}, content_type='application/json'):
        return requests.put(url, data=json.dumps(data))

    # def post(self, url, data={}, content_type='application/json'):
    #     return self._request(url, data, 'POST', content_type)

    # def delete(self, url, data=None, content_type='application/json'):
    #     return self._request(url, data, 'DELETE', content_type)
