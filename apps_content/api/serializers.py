from rest_framework import serializers

from apps_content.biblioteca.models import Store, Author, Publisher, Book


class StoreSerializer(serializers.HyperlinkedModelSerializer):
    books = serializers.StringRelatedField(many=True)#Se usa para relaciones inversas

    class Meta:
        model = Store
        fields = ('id', 'url', 'name', 'direction', 'books')


class AuthorSerializer(serializers.ModelSerializer):
    books = serializers.SlugRelatedField(many=True, read_only=True, slug_field='name')

    class Meta:
        model = Author
        fields = ('id','name', 'age', 'salutation', 'email', 'created', 'modified', 'books')


class PublisherSerializer(serializers.ModelSerializer):
    #PrimaryKeyRelatedField se puede usar para representar el objetivo de la relación usando su clave principal
    books = serializers.PrimaryKeyRelatedField(many=True, read_only=True) #queryset=Book.objects.all()

    class Meta:
        model = Publisher
        fields = ('id', 'name', 'address', 'city', 'state_province', 'country', 'website', 'books')


class BookSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True)
    #authors = serializers.ReadOnlyField(source='authors.name') Esto no se puede por que es una relacion a muchos
    publisher = serializers.ReadOnlyField(source='publisher.name')
    #publisher = PublisherSerializer(many=True) Esto no se puede
    class Meta:
        model = Book
        fields = ('id', 'name', 'book_code', 'pages', 'price', 'rating', 'authors', 'publisher', 'publication_date', 'gender', 'created_by')
