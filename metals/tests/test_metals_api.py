from metals.api_clients.metals_api import MetalsAPI


class TestMetalsAPI:

    def test_api_latest(self):
        metals_api = MetalsAPI()
        metals_api.fetch_latest()
        pass