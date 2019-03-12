from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, ListView, TemplateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django import forms

from .forms import BookModelForm

from .models import University, Store, Book, Student, Author, Loan, Publisher


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

    def get_form(self, form_class=None):
        form = super(BookCreateView, self).get_form(form_class=form_class)
        # Modificar en tiempo real
        form.fields['name'].widget = forms.TextInput(attrs={'class': 'form-control mb-4', 'placeholder': 'Nombre del usuario'})
        return form


class BookUpdateView(UpdateView):
    model = Book
    form_class = BookModelForm
    template_name = 'book/update-book.html'
    success_url = reverse_lazy('list_book')

    def form_valid(self, form):
        book = form.save(commit=False)
        book.created_by = self.request.user
        book.save()
        return super(BookUpdateView, self).form_valid(form)


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


class AuthorListView(ListView):
    template_name = 'author/list-author.html'
    context_object_name = 'authors'

    def get_queryset(self):
        return Author.objects.all()


class AuthorDetailView(DetailView):
    template_name = 'author/detail-author.html'
    context_object_name = 'author'

    def get_object(self, queryset=None):
        return get_object_or_404(Author, pk=self.kwargs['pk'])


class AuthorCreateView(CreateView):
    model = Author
    template_name = 'author/create-author.html'
    fields = ('name', 'age', 'salutation', 'email')

    def get_success_url(self):
        return reverse_lazy('create_author')


class AuthorUpdateView(UpdateView):
    model = Author
    template_name = 'author/update-author.html'
    fields = ('name', 'age', 'salutation', 'email')
    success_url = reverse_lazy('list_author')

    def get_object(self, queryset=None):
        return get_object_or_404(Author, pk=self.kwargs['pk'])

    def get_success_url(self):
        return reverse_lazy('update_author', args=[self.object.pk])


class AuthorDeleteView(DeleteView):
    model = Author
    template_name = 'author/delete-author.html'
    context_object_name = 'author'

    def get_object(self, queryset=None):
        return get_object_or_404(Author, pk=self.kwargs['pk'])

    def get_success_url(self):
        return reverse_lazy('list_author')


class LoanListView(ListView):
    template_name = 'loan/list-loan.html'
    context_object_name = 'loans'

    def get_queryset(self):
        return Loan.objects.all()


class LoanDetailView(DetailView):
    template_name = 'loan/detail-loan.html'
    context_object_name = 'loan'

    def get_object(self, queryset=None):
        return get_object_or_404(Loan, pk=self.kwargs['pk'])


class LoanCreateView(CreateView):
    model = Loan
    template_name = 'loan/create-loan.html'
    fields = ('order_number', 'book', 'student', 'date_s', 'date_e', 'date_d')

    def get_success_url(self):
        return reverse_lazy('create_loan')


class LoanUpdateView(UpdateView):
    template_name = 'loan/update-loan.html'
    fields = ('order_number', 'book', 'student', 'date_s', 'date_e', 'date_d')

    def get_object(self, queryset=None):
        return get_object_or_404(Loan, pk=self.kwargs['pk'])

    def get_success_url(self):
        return reverse_lazy('update_loan', args=[self.object.pk])


class LoanDeleteView(DeleteView):
    template_name = 'loan/delete-loan.html'
    context_object_name = 'loan'

    def get_object(self, queryset=None):
        return get_object_or_404(Loan, pk=self.kwargs['pk'])

    def get_success_url(self):
        return reverse_lazy('list_loan')


class PublisherListView(ListView):
    template_name = 'publisher/list-publisher.html'
    context_object_name = 'publishers'

    def get_queryset(self):
        return Publisher.objects.all()


class PublisherDetailView(DetailView):
    template_name = 'publisher/detail-publisher.html'
    context_object_name = 'publisher'

    def get_object(self, queryset=None):
        return get_object_or_404(Publisher, pk=self.kwargs['pk'])


class PublisherCreateView(CreateView):
    model = Publisher
    template_name = 'publisher/create-publisher.html'
    fields = ('name', 'address', 'city', 'state_province', 'country', 'website')

    def get_success_url(self):
        return reverse_lazy('create_publisher')


class PublisherUpdateView(UpdateView):
    template_name = 'publisher/update-publisher.html'
    fields = ('name', 'address', 'city', 'state_province', 'country', 'website')

    def get_object(self, queryset=None):
        return get_object_or_404(Publisher, pk=self.kwargs['pk'])

    def get_success_url(self):
        return reverse_lazy('update_publisher', args=[self.object.pk])


class PublisherDeleteView(DeleteView):
    template_name = 'publisher/delete-publisher.html'
    context_object_name = 'publisher'

    def get_object(self, queryset=None):
        return get_object_or_404(Loan, pk=self.kwargs['pk'])

    def get_success_url(self):
        return reverse_lazy('list_publisher')
