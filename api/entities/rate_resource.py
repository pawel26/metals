from api.entities.metal_resource import MetalResource
from api.models import Rate


class RateResource:

    def __init__(self, date, currency, unit, rates):
        self.date = date
        self.currency = currency
        self.unit = unit
        self.rates = rates

    def create_rates(self):
        silver = MetalResource(self.date, "AG").get_instance()
        gold = MetalResource(self.date, "AU").get_instance()
        for rate, value in self.rates.items():
            if rate == "XAG":
                self.create_rate(silver, rate, value)
            elif rate == "XAU":
                self.create_rate(gold, rate, value)

    def create_rate(self, metal, metal_code, rate_value):
        rate = Rate()
        rate.metal_code = metal_code
        rate.metal_rate = 1 / rate_value
        rate.metal = metal
        rate.currency = self.currency
        rate.unit = self.unit
        rate.source = "Metals API"
        rate.save()
