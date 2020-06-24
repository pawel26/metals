import json
import requests

from metals.helpers.url import add_query_params as _add_query_params

DATA = "data"
CONTENT_TYPE = "content-type"
JSON_TYPE = "application/json"
HEADERS = "headers"
SESSION_EXPIRED_REASON = "10"
PARAMS = "params"


class Resource:

    def __init__(self, base_url, session=None):

        self.base_url = base_url
        self.session = session

    def __repr__(self):
        return '<instance for %s>' % (repr(self.__class__)[8:-2])

    def _request(self, method, url, **kwargs):
        return (self.session or requests).request(
            method=method, url=url, **kwargs)

    def request(self, method, **kwargs):
        has_content_type = self.has_content_type(kwargs)
        if method == 'POST' and not has_content_type:
            kwargs = self.update_request_kwargs(kwargs)

        if PARAMS not in kwargs:
            kwargs[PARAMS] = {}

        response = self._request(method=method, url=self.base_url, **kwargs)
        # TODO add HTTP error handling

        return response

    @staticmethod
    def has_content_type(named_params_dict):
        return CONTENT_TYPE in named_params_dict.get(HEADERS, {})

    @staticmethod
    def update_request_kwargs(kwargs):
        kwargs[DATA] = json.dumps(kwargs.pop(DATA, {}))
        if HEADERS not in kwargs:
            kwargs[HEADERS] = {}
        kwargs[HEADERS][CONTENT_TYPE] = JSON_TYPE

        return kwargs

    def get(self, **kwargs):
        return self.request('GET', **kwargs)

    def post(self, **kwargs):
        return self.request('POST', **kwargs)

    def add_query_params(self, *args, **kwargs):
        new_url = _add_query_params(self.base_url, *args, **kwargs)
        return self.__class__(base_url=new_url, session=self.session)
