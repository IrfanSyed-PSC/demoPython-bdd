from cachetools import TTLCache
from requests.adapters import HTTPAdapter
from requests.exceptions import RequestException
import requests

## Define cache
cache = TTLCache(maxsize=100, ttl=5)


class RequestsAPI:
    def __init__(self, base_url):
        self.session = requests.Session()
        self.session.base_url = base_url
        retries = HTTPAdapter(max_retries=3)
        self.session.mount('http://', retries)
        self.session.mount('https://', retries)

    def get(self, endpoint, params=None):
        url = self.session.base_url + endpoint
        response = self.session.get(url, params=params)
        return response

    def post(self, endpoint, data=None):
        url = self.session.base_url + endpoint
        response = requests.post(url, json=data)
        return response

    def put(self, endpoint, data=None):
        url = self.session.base_url + endpoint
        response = requests.put(url, json=data)
        return response

    def delete(self, endpoint):
        url = self.session.base_url + endpoint
        response = requests.delete(url)
        return response