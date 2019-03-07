from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.http import Http404

from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView

from apps_content.api.serializers import (
    StoreSerializer, AuthorSerializer, PublisherSerializer, BookSerializer, UniversitySerializer,
    StudentSerializer, LoanSerializer
)
from apps_content.biblioteca.models import Store, Author, Publisher, Book, University, Student, Loan


class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer


class AuthorListAPIView(ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorListCreateAPIView(APIView):

    def get(self, request, format=None):
        author = Author.objects.all()
        serializer = AuthorSerializer(author, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AuthorGetPutDeleteAPIView(APIView):

    def get_object(self, pk):
        try:
            return Author.objects.get(pk=pk)
        except Author.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        author = self.get_object(pk)
        serializer = AuthorSerializer(author)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        author = self.get_object(pk)
        serializer = AuthorSerializer(author, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, pk, request, format=None):
        author = self.get_object(pk)
        author.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


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


class BookListAPIView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookRetrieveAPIView(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookCreateAPIView(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookUpdateAPIView(UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDestroyAPIView(DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class UniversityListAPIView(ListAPIView):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer


class UniversityRetrieveAPIView(RetrieveAPIView):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer


class UniversityCreateAPIView(CreateAPIView):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer


class StudentListAPIView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentRetrieveAPIView(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentCreateAPIView(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class LoanListAPIView(ListAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer


class LoanRetrieveAPIView(RetrieveAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer


class LoanCreateAPIView(CreateAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer


class LoanUpdateAPIView(UpdateAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer


class LoanDestroyAPIView(DestroyAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
