from django.contrib import admin
from django.urls import include, path


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls')),
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]