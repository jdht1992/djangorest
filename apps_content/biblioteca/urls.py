from django.urls import path
from .views import (
    HomePageView, UniversityListView, UniversityCreateView, UniversityDetailView, UniversityUpdateView,
    StoreListView, StoreCreateView, StoreDetailView, StoreUpdateView,
    BookListView, BookDetailView, BookCreateView, BookUpdateView,
    StudentListView, StudentDetailView, StudentCreateView, StudentUpdateView
)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('university/list', UniversityListView.as_view(), name='list_university'),
    path('university/create', UniversityCreateView.as_view(), name='create_university'),
    path('university/detail/<int:pk>', UniversityDetailView.as_view(), name='detail_university'),
    path('university/update/<int:pk>', UniversityUpdateView.as_view(), name='update_university'),
    #Store
    path('store/list', StoreListView.as_view(), name='list_store'),
    path('store/create', StoreCreateView.as_view(), name='create_store'),
    path('store/detail/<int:pk>', StoreDetailView.as_view(), name='detail_store'),
    path('store/update/<int:pk>', StoreUpdateView.as_view(), name='update_store'),
    #book
    path('book/list', BookListView.as_view(), name='list_book'),
    path('book/detail/<int:pk>', BookDetailView.as_view(), name='detail_book'),
    path('book/create', BookCreateView.as_view(), name='create_book'),
    path('book/update/<int:pk>', BookUpdateView.as_view(), name='update_book'),
    #student
    path('student/list', StudentListView.as_view(), name='list_student'),
    path('student/detail/<int:pk>', StudentDetailView.as_view(), name='detail_student'),
    path('student/create', StudentCreateView.as_view(), name='create_student'),
    path('student/update/<int:pk>', StudentUpdateView.as_view(), name='update_student'),
]

