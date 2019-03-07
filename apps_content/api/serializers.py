from rest_framework import serializers

from apps_content.biblioteca.models import Store, Author, Publisher


class StoreSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Store
        fields = ('id', 'url', 'name', 'direction')


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ('name', 'age', 'salutation', 'email', 'created', 'modified')


class PublisherSerializer(serializers.ModelSerializer):
    #PrimaryKeyRelatedField se puede usar para representar el objetivo de la relación usando su clave principal
    book = serializers.PrimaryKeyRelatedField(many=True, read_only=True) #queryset=Book.objects.all()

    class Meta:
        model = Publisher
        fields = ('id', 'name', 'address', 'city', 'state_province', 'country', 'website', 'book')
