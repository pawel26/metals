from django.core.management import BaseCommand

from api.entities.rate_resource import RateResource
from api_clients.metals_api import MetalsAPI


class Command(BaseCommand):
    help = 'Populating database with daily silver and gold rates'

    def add_arguments(self, parser):
        parser.add_argument('--source', type=str,
                            help='Indicates the source API for fetching rates')

    def handle(self, *args, **options):
        source = options['source']
        if source == "MetalsAPI":
            api_source = MetalsAPI()
            latest = api_source.fetch_latest()
            rate_resource = RateResource(latest["date"], latest["base"],
                                     latest["unit"], latest["rates"])
            rate_resource.create_rates()





 # latest = {
        #     "success": True,
        #     "timestamp":1592737920,
        #     "date": "2020-06-24",
        #     "base": "USD",
        #     "rates": {
        #         "USD": 1,
        #         "XAG": 0.05688929376, "XAU": 0.00057440754
        #     },
        #     "unit": "per ounce"}