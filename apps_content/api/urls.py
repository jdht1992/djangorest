from django.urls import path, include
from rest_framework import routers
from apps_content.api.views import StoreViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register('store', StoreViewSet)


urlpatterns = [
    path('', include(router.urls)),
]


