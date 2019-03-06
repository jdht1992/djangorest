from rest_framework import serializers

from apps_content.biblioteca.models import Store

class StoreSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Store
        fields = ('id', 'url', 'name', 'direction')
