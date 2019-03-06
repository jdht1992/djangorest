from rest_framework import viewsets

from apps_content.api.serializers import StoreSerializer

from apps_content.biblioteca.models import Store


class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
