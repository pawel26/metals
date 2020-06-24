from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'metals', views.MetalViewSet)
router.register(r'silver', views.SilverViewSet)
router.register(r'gold', views.GoldViewSet)
router.register(r'rates', views.RateViewSet)
router.register(r'raport', views.RaportViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
