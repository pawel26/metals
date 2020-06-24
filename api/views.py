from drf_renderer_xlsx.mixins import XLSXFileMixin
from drf_renderer_xlsx.renderers import XLSXRenderer
from rest_framework import viewsets
from rest_framework.viewsets import ReadOnlyModelViewSet

from .pagination import StandardResultsSetPagination, \
    HeaderLimitOffsetPagination
from .serializers import MetalSerializer, RateSerializer

from.models import Metal, Rate


class MetalViewSet(viewsets.ModelViewSet):
    queryset = Metal.objects.all()
    serializer_class = MetalSerializer
    pagination_class = StandardResultsSetPagination
    filterset_fields = {
        'metal_name': ['exact', 'isnull'],
        'datetime': ['exact', 'lte', 'gte']
    }


class SilverViewSet(viewsets.ModelViewSet):
    queryset = Metal.silver
    serializer_class = MetalSerializer #own serializers
    filterset_fields = {
        'metal_name': ['exact', 'isnull'],
        'datetime': ['exact', 'lte', 'gte']
    }


class GoldViewSet(viewsets.ModelViewSet):
    queryset = Metal.gold
    serializer_class = MetalSerializer
    filterset_fields = {
        'metal_name': ['exact', 'isnull'],
        'datetime': ['exact', 'lte', 'gte']
    }


class RateViewSet(viewsets.ModelViewSet):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer
    pagination_class = StandardResultsSetPagination
    filterset_fields = {
        'metal_code': ['exact', 'isnull'],
        'source': ['exact', 'isnull'],
        'currency': ['exact', 'isnull'],
        'unit': ['exact', 'isnull'],
        'timestamp': ['exact', 'lte', 'gte'],
        'metal_rate': ['exact', 'lte', 'gte']
    }


class RaportViewSet(XLSXFileMixin, ReadOnlyModelViewSet):
    queryset = Metal.objects.all()
    serializer_class = MetalSerializer
    renderer_classes = [XLSXRenderer]
    filename = 'raport.xlsx'
