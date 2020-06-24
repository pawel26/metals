from django.db.models import Avg
from rest_framework import serializers

from .models import Metal, Rate


class RateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rate
        fields = [
            'id', 'timestamp', 'metal_code', 'metal_rate', 'source', 'unit', 'currency'
        ]


class MetalSerializer(serializers.ModelSerializer):
    rates = RateSerializer(many=True)
    total_rates = serializers.SerializerMethodField()
    rates_average = serializers.SerializerMethodField()

    class Meta:
        model = Metal
        fields = ['id', 'metal_name', 'datetime',
                  'rates', 'total_rates', 'rates_average']

    def get_total_rates(self, obj):
        return obj.rates.count()

    def get_rates_average(self, obj):
        return obj.rates.values('metal_rate').aggregate(
            Avg('metal_rate'))["metal_rate__avg"]
