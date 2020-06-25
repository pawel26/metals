import datetime

from django.test import TestCase
from api.models import Metal, Rate


class MetalTest(TestCase):
    """ Test module for Puppy model """

    def setUp(self):
        self.now = datetime.datetime.now()
        Metal.objects.create(metal_name='silver')
        Metal.objects.create(metal_name='gold')

    def test_metal_created_in_db(self):
        silver = Metal.objects.get(metal_name='silver')
        gold = Metal.objects.get(metal_name='gold')

        assert isinstance(silver, Metal)
        assert isinstance(gold, Metal)


class RateTest(TestCase):
    """ Test module for Puppy model """

    def setUp(self):
        self.now = datetime.datetime.now()
        Metal.objects.create(metal_name='silver')
        Metal.objects.create(metal_name='gold')

    def test_create_rate_for_silver(self):
        silver = Metal.objects.get(metal_name='silver')
        rate = Rate()
        rate.metal_code = "AG"
        rate.metal_rate = 17.3456
        rate.metal = silver
        rate.currency = "USD"
        rate.unit = "ounce"
        rate.source = "Dummy API"
        rate.save()
        silver_rate = Rate.objects.get(metal=silver)

        assert isinstance(silver_rate, Rate)
        assert silver_rate.metal == silver

    def test_create_rate_for_gold(self):
        gold = Metal.objects.get(metal_name='gold')
        rate = Rate()
        rate.metal_code = "AG"
        rate.metal_rate = 17.3456
        rate.metal = gold
        rate.currency = "USD"
        rate.unit = "ounce"
        rate.source = "Dummy API"
        rate.save()
        gold_rate = Rate.objects.get(metal=gold)

        assert isinstance(gold_rate, Rate)
        assert gold_rate.metal == gold
