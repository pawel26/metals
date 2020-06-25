from unittest import TestCase
from rest_framework.test import APIRequestFactory

from api.models import Metal, Rate
from api.views import MetalViewSet, GoldViewSet, SilverViewSet, RateViewSet


class GetMetalsTest(TestCase):

    def setUp(self):
        Metal.objects.create(metal_name='silver')
        Metal.objects.create(metal_name='gold')

    def test_metal_view_set(self):
        factory = APIRequestFactory()
        view = MetalViewSet.as_view(actions={'get': 'list'})

        request = factory.get('metals')
        response = view(request)

        assert response.status_code == 200


class GetGoldTest(TestCase):

    def setUp(self):
        Metal.objects.create(metal_name='gold')

    def test_gold_metal_view_set(self):
        factory = APIRequestFactory()
        view = GoldViewSet.as_view(actions={'get': 'list'})

        request = factory.get('gold')
        response = view(request)

        assert response.status_code == 200


class GetSilverTest(TestCase):

    def setUp(self):
        Metal.objects.create(metal_name='silver')

    def test_gold_metal_view_set(self):
        factory = APIRequestFactory()
        view = SilverViewSet.as_view(actions={'get': 'list'})

        request = factory.get('silver')
        response = view(request)

        assert response.status_code == 200


class GetRatesTest(TestCase):

    def setUp(self):
        Metal.objects.create(metal_name='silver')
        silver = Metal.objects.get(id=1)
        rate = Rate()
        rate.metal_code = "AG"
        rate.metal_rate = 17.3456
        rate.metal = silver
        rate.currency = "USD"
        rate.unit = "ounce"
        rate.source = "Dummy API"
        rate.save()

    def test_rates_view_set(self):
        factory = APIRequestFactory()
        view = RateViewSet.as_view(actions={'get': 'list'})

        request = factory.get('rates')
        response = view(request)

        assert response.status_code == 200