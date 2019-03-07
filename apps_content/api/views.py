from rest_framework import viewsets
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView

from apps_content.api.serializers import StoreSerializer, AuthorSerializer, PublisherSerializer

from apps_content.biblioteca.models import Store, Author, Publisher


class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer


class AuthorListAPIView(ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class PublisherListAPIView(ListAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer


class PublisherRetrieveAPIView(RetrieveAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    #se debe utilizar para realizar la búsqueda de objetos de instancias de modelos individuales
    lookup_field = 'name'


class PublisherCreateAPIView(CreateAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer


class PublisherUpdateAPIView(UpdateAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer


class PublisherDestroyPIView(DestroyAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
