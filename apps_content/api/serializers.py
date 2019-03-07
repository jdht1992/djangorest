from rest_framework import serializers

from apps_content.biblioteca.models import Store, Author, Publisher, Book, University, Student, Loan


class StoreSerializer(serializers.HyperlinkedModelSerializer):
    books = serializers.StringRelatedField(many=True)#Se usa para relaciones inversas

    class Meta:
        model = Store
        fields = ('id', 'url', 'name', 'direction', 'books')


class AuthorSerializer(serializers.ModelSerializer):
    books = serializers.SlugRelatedField(many=True, read_only=True, slug_field='name')

    class Meta:
        model = Author
        fields = ('id', 'name', 'age', 'salutation', 'email', 'created', 'modified', 'books')


class AuthorListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ('id', 'name')


class PublisherSerializer(serializers.ModelSerializer):
    #PrimaryKeyRelatedField se puede usar para representar el objetivo de la relación usando su clave principal
    books = serializers.PrimaryKeyRelatedField(many=True, read_only=True) #queryset=Book.objects.all()

    class Meta:
        model = Publisher
        fields = ('id', 'name', 'address', 'city', 'state_province', 'country', 'website', 'books')


class BookSerializer(serializers.ModelSerializer):
    authors = AuthorListSerializer(many=True)
    publisher = serializers.ReadOnlyField(source='publisher.name')
    created_by = serializers.ReadOnlyField(source='created_by.username')

    class Meta:
        model = Book
        fields = ('id', 'name', 'book_code', 'pages', 'price', 'rating', 'authors', 'publisher', 'publication_date', 'gender', 'created_by')


class BookListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('id', 'name')


class UniversitySerializer(serializers.ModelSerializer):
    students = serializers.SlugRelatedField(many=True, read_only=True, slug_field='first_name')

    class Meta:
        model = University
        fields = ('id', 'full_name', 'address', 'city', 'university_type', 'students')


class StudentSerializer(serializers.ModelSerializer):
    university = serializers.ReadOnlyField(source='university.full_name')

    class Meta:
        model = Student
        fields = ('id', 'first_name', 'last_name', 'university', 'marital_status', 'gender', 'address', 'telephone_number',
        'additional_data', 'birthday',)


class LoanSerializer(serializers.ModelSerializer):
    book = BookListSerializer(many=True)
    student = serializers.ReadOnlyField(source='student.first_name')

    class Meta:
        model = Loan
        fields = ('id', 'order_number', 'student', 'date_s', 'date_e', 'date_d', 'book')
