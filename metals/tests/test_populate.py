from metals.api.management.commands.populate import PopulateRates


class TestPopulateRates:

    def test_populate(self):
        PopulateRates().populate()