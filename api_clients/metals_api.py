from api_wrappers.api import Api
from api_wrappers.metals_interface import MetalsInterface
from .config import METALS_API
from api_wrappers.helpers.endpoints import Endpoint


@MetalsInterface.register
class MetalsAPI:

    base_url = METALS_API.get('base_url', None)
    api_key = METALS_API.get('api_key', None)
    currency = METALS_API.get('default_currency', 'USD')
    rates_for_metals = METALS_API.get('metals_to_fetch', 'XAU,XAG')
    api = Api(base_url)

    def fetch_latest(self):
        response = self.api[Endpoint.LATEST.value].add_query_params(
            access_key=self.api_key,
            base=self.currency,
            symbols=self.rates_for_metals
        ).get().json()
        return response

    def fetch_historical(self, by_date):
        response = self.api[by_date].add_query_params(
            access_key=self.api_key,
            base=self.currency,
            symbols=self.rates_for_metals
        ).get().json()

        return response

    def rate_fluctuation(self, rate_type='weekly', start_date=None, end_date=None):
        query = self.api[Endpoint.FLUCTUATION.value].add_query_params(
            access_key=self.api_key,
            base=self.currency,
            symbols=self.rates_for_metals,
            type=rate_type
        )
        if start_date and end_date:
            query.add_query_params(start_date=start_date, end_date=end_date)
        response = query.get().json()

        return response
