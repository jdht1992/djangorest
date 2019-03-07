from django.urls import path, include
from rest_framework import routers
from apps_content.api.views import (
    StoreViewSet,
    AuthorListCreateAPIView, AuthorGetPutDeleteAPIView,
    PublisherListAPIView, PublisherRetrieveAPIView, PublisherCreateAPIView, PublisherUpdateAPIView, PublisherDestroyPIView,
    BookListAPIView, BookRetrieveAPIView, BookCreateAPIView, BookUpdateAPIView, BookDestroyAPIView,
    UniversityListAPIView, UniversityRetrieveAPIView, UniversityCreateAPIView,
    StudentListAPIView, StudentRetrieveAPIView, StudentCreateAPIView,
    LoanListAPIView, LoanRetrieveAPIView, LoanCreateAPIView, LoanUpdateAPIView, LoanDestroyAPIView
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
    #Book
    path('book/', BookListAPIView.as_view()),
    path('book/detail/<int:pk>/', BookRetrieveAPIView.as_view()),
    path('book/create/', BookCreateAPIView.as_view()),
    path('book/update/<int:pk>/', BookUpdateAPIView.as_view()),
    path('book/delete/<int:pk>/', BookDestroyAPIView.as_view()),
    #University
    path('university/', UniversityListAPIView.as_view()),
    path('university/detail/<int:pk>/', UniversityRetrieveAPIView.as_view()),
    path('university/create/', UniversityCreateAPIView.as_view()),
    #Student
    path('student/', StudentListAPIView.as_view()),
    path('student/detail/<int:pk>/', StudentRetrieveAPIView.as_view()),
    path('student/create/', StudentCreateAPIView.as_view()),
    #Loan
    path('loan/', LoanListAPIView.as_view(), name='loan_list'),
    path('loan/<int:pk>/', LoanRetrieveAPIView.as_view(), name='loan_detail'),
    path('loan/create/', LoanCreateAPIView.as_view(), name='loan_create'),
    path('loan/update/<int:pk>/', LoanUpdateAPIView.as_view(), name='loan_update'),
    path('loan/delete/<int:pk>/', LoanDestroyAPIView.as_view(), name='loan_delete'),
]
