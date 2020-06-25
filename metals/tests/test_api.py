from api_wrappers.api import Api


class TestMetalsAPI:

    def test_api_object(self):
        api = Api('https://metals-api.com/api//latest/')
        response = api['latest'].get()

        assert response.status_code == 200