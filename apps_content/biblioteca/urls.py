from django.urls import path
from .views import (
    HomePageView,
    UniversityListView, UniversityCreateView, UniversityDetailView, UniversityUpdateView, UniversityDeleteView,
    StoreListView, StoreCreateView, StoreDetailView, StoreUpdateView, StoreDeleteView,
    BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView,
    StudentListView, StudentDetailView, StudentCreateView, StudentUpdateView, StudentDeleteView,
    AuthorListView, AuthorDetailView, AuthorCreateView, AuthorUpdateView, AuthorDeleteView,
    LoanListView, LoanDetailView, LoanCreateView, LoanUpdateView, LoanDeleteView,
    PublisherListView, PublisherDetailView, PublisherCreateView, PublisherUpdateView, PublisherDeleteView,
)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('university/list', UniversityListView.as_view(), name='list_university'),
    path('university/create', UniversityCreateView.as_view(), name='create_university'),
    path('university/detail/<int:pk>', UniversityDetailView.as_view(), name='detail_university'),
    path('university/update/<int:pk>', UniversityUpdateView.as_view(), name='update_university'),
    path('university/delete/<int:pk>', UniversityDeleteView.as_view(), name='delete_university'),
    # Store
    path('store/list', StoreListView.as_view(), name='list_store'),
    path('store/create', StoreCreateView.as_view(), name='create_store'),
    path('store/detail/<int:pk>', StoreDetailView.as_view(), name='detail_store'),
    path('store/update/<int:pk>', StoreUpdateView.as_view(), name='update_store'),
    path('store/delete/<int:pk>', StoreDeleteView.as_view(), name='delete_store'),
    # Book
    path('book/list', BookListView.as_view(), name='list_book'),
    path('book/detail/<int:pk>', BookDetailView.as_view(), name='detail_book'),
    path('book/create', BookCreateView.as_view(), name='create_book'),
    path('book/update/<int:pk>', BookUpdateView.as_view(), name='update_book'),
    path('book/delete/<int:pk>', BookDeleteView.as_view(), name='delete_book'),
    # Student
    path('student/list', StudentListView.as_view(), name='list_student'),
    path('student/detail/<int:pk>', StudentDetailView.as_view(), name='detail_student'),
    path('student/create', StudentCreateView.as_view(), name='create_student'),
    path('student/update/<int:pk>', StudentUpdateView.as_view(), name='update_student'),
    path('student/delete/<int:pk>', StudentDeleteView.as_view(), name='delete_student'),
    # Author
    path('author/list/', AuthorListView.as_view(), name='list_author'),
    path('author/detail/<int:pk>', AuthorDetailView.as_view(), name='detail_author'),
    path('author/create', AuthorCreateView.as_view(), name='create_author'),
    path('author/update/<int:pk>', AuthorUpdateView.as_view(), name='update_author'),
    path('author/delete/<int:pk>', AuthorDeleteView.as_view(), name='delete_author'),
    # Loan
    path('loan/list', LoanListView.as_view(), name='list_loan'),
    path('loan/detail/<int:pk>', LoanDetailView.as_view(), name='detail_loan'),
    path('loan/create', LoanCreateView.as_view(), name='create_loan'),
    path('loan/update/<int:pk>', LoanUpdateView.as_view(), name='update_loan'),
    path('loan/delete/<int:pk>', LoanDeleteView.as_view(), name='delete_loan'),
    # Publisher
    path('publisher/list', PublisherListView.as_view(), name='list_publisher'),
    path('publisher/detail/<int:pk>', PublisherDetailView.as_view(), name='detail_publisher'),
    path('publisher/create', PublisherCreateView.as_view(), name='create_publisher'),
    path('publisher/update/<int:pk>', PublisherUpdateView.as_view(), name='update_publisher'),
    path('publisher/delete/<int:pk>', PublisherDeleteView.as_view(), name='delete_publisher'),
]
