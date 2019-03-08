from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, ListView, TemplateView, DetailView, UpdateView
from django.urls import reverse_lazy

from .forms import BookModelForm

from .models import University, Store, Book, Student


class HomePageView(TemplateView):
    template_name = 'home.html'


class UniversityListView(ListView):
    model = University
    template_name = 'university/list-university.html'
    context_object_name = 'universities'


class UniversityDetailView(DetailView):
    model = University
    template_name = 'university/detail-university.html'
    context_object_name = 'university'


class UniversityCreateView(CreateView):
    model = University
    template_name = 'university/create-university.html'
    fields = ('full_name', 'address', 'city')
    success_url = reverse_lazy('list_university')


class UniversityUpdateView(UpdateView):
    model = University
    template_name = 'university/update-university.html'
    fields = ('full_name', 'address', 'city')
    success_url = reverse_lazy('list_university')


class StoreListView(ListView):
    template_name = 'store/list-store.html'
    context_object_name = 'stores'

    def get_queryset(self):
        return Store.objects.all()


class StoreDetailView(DetailView):
    template_name = 'store/detail-store.html'
    context_object_name = 'store'

    def get_object(self, queryset=None):
        return get_object_or_404(Store, pk=self.kwargs['pk'])


class StoreCreateView(CreateView):
    model = Store
    template_name = 'store/create-store.html'
    fields = ('name', 'direction', 'books')

    def get_success_url(self):
        return reverse_lazy('create_store')


class StoreUpdateView(UpdateView):
    template_name = 'store/update-store.html'
    fields = ('name', 'direction', 'books')

    def get_object(self, queryset=None):
        return get_object_or_404(Store, pk=self.kwargs['pk'])

    def get_success_url(self):
        return reverse_lazy('update_store', args=[self.object.pk])


class BookListView(ListView):
    template_name = 'book/list-book.html'
    context_object_name = 'books'

    def get_queryset(self):
        return Book.objects.all()


class BookDetailView(DetailView):
    template_name = 'book/detail-book.html'
    context_object_name = 'book'

    def get_object(self, queryset=None):
        return get_object_or_404(Book, pk=self.kwargs['pk'])


class BookCreateView(CreateView):
    model = Book
    form_class = BookModelForm
    template_name = 'book/create-book.html'
    success_url = reverse_lazy('list_book')

    def form_valid(self, form):
        book = form.save(commit=False)
        book.created_by = self.request.user
        book.save()
        return super(BookCreateView, self).form_valid(form)


class BookUpdateView(UpdateView):
    template_name = 'book/update-book.html'
    fields = ('name', 'book_code', 'pages', 'price', 'rating', 'authors', 'publisher', 'publication_date', 'gender')

    def form_valid(self, form):
        book = form.save(commit=False)
        book.created_by = self.request.user
        book.save()
        return super(BookUpdateView, self).form_valid(form)

    def get_object(self, queryset=None):
        return get_object_or_404(Book, pk=self.kwargs['pk'])

    def get_success_url(self):
        return reverse_lazy('update_book', args=[self.object.pk])


class StudentListView(ListView):
    model = Student
    template_name = 'student/list-student.html'
    context_object_name = 'students'


class StudentDetailView(DetailView):
    model = Student
    template_name = 'student/detail-student.html'
    context_object_name = 'student'


class StudentCreateView(CreateView):
    model = Student
    fields = ('first_name', 'last_name', 'university', 'marital_status', 'gender', 'address', 'telephone_number', 'additional_data', 'birthday', 'image')
    template_name = 'student/create-student.html'
    success_url = reverse_lazy('list_student')


class StudentUpdateView(UpdateView):
    model = Student
    fields = ('first_name', 'last_name', 'university', 'marital_status', 'gender', 'address', 'telephone_number', 'additional_data', 'birthday', 'image')
    template_name = 'student/update-student.html'
    success_url = reverse_lazy('list_student')
