from django.urls import path, include
from rest_framework import routers
from apps_content.api.views import (
    StoreViewSet,
    AuthorListCreateAPIView, AuthorGetPutDeleteAPIView,
    PublisherListAPIView, PublisherRetrieveAPIView, PublisherCreateAPIView, PublisherUpdateAPIView, PublisherDestroyPIView
)

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register('store', StoreViewSet)


urlpatterns = [
    path('', include(router.urls)),
    #Author
    path('author/', AuthorListCreateAPIView.as_view()),
    path('author/<int:pk>/', AuthorGetPutDeleteAPIView.as_view()),
    #Publisher
    path('publisher', PublisherListAPIView.as_view(), name='api_list_publisher'),
    path('publisher/detail/<name>/', PublisherRetrieveAPIView.as_view()),
    path('publisher/create/', PublisherCreateAPIView.as_view()),
    path('publisher/update/<int:pk>/', PublisherUpdateAPIView.as_view()),
    path('publisher/delete/<int:pk>/', PublisherDestroyPIView.as_view()),
]
