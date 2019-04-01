from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, ListView, TemplateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Avg, Max, Min, FloatField
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django import forms

from .forms import BookModelForm
from .models import University, Store, Book, Student, Author, Loan, Publisher


class HomePageView(TemplateView):
    template_name = 'home.html'

    #def get_context_data(self, *args, **kwargs):
    #    context = super(HomePageView, self).get_context_data(*args, **kwargs)
    #    context['today'] = datetime.date.today()
    #    return context


class UniversityListView(ListView):
    model = University
    template_name = 'university/list-university.html'
    context_object_name = 'universities'


class UniversityDetailView(LoginRequiredMixin, DetailView):
    model = University
    template_name = 'university/detail-university.html'
    context_object_name = 'university'


class UniversityCreateView(LoginRequiredMixin, CreateView):
    model = University
    template_name = 'university/create-university.html'
    fields = ('full_name', 'address', 'city', 'university_type')
    success_url = reverse_lazy('list_university')


class UniversityUpdateView(LoginRequiredMixin, UpdateView):
    model = University
    template_name = 'university/update-university.html'
    fields = ('full_name', 'address', 'city', 'university_type')

    def get_success_url(self):
        return reverse_lazy('list_university', pk=self.kwargs['pk'])


class UniversityDeleteView(LoginRequiredMixin, DeleteView):
    model = University
    template_name = 'university/delete-university.html'
    context_object_name = 'university'
    success_url = reverse_lazy('list_university')


class StoreListView(ListView):
    queryset = Store.objects.all().values('pk', 'name')
    template_name = 'store/list-store.html'
    context_object_name = 'stores'


class StoreDetailView(LoginRequiredMixin, DetailView):
    queryset = Store.objects.prefetch_related('books')
    template_name = 'store/detail-store.html'
    context_object_name = 'store'


class StoreCreateView(LoginRequiredMixin, CreateView):
    model = Store
    template_name = 'store/create-store.html'
    fields = ('name', 'direction', 'books')
    success_url = reverse_lazy('create_store')


class StoreUpdateView(LoginRequiredMixin, UpdateView):
    queryset = Store.objects.prefetch_related('books')
    template_name = 'store/update-store.html'
    fields = ('name', 'direction', 'books')

    def get_success_url(self):
        return reverse_lazy('update_store', args=[self.object.pk])


class StoreDeleteView(LoginRequiredMixin, DeleteView):
    queryset = Store.objects.prefetch_related('books')
    template_name = 'store/delete-store.html'
    context_object_name = 'store'
    success_url = reverse_lazy('list_store')


class BookListView(ListView):
    #queryset = Book.objects.all().values('pk', 'name')
    template_name = 'book/list-book.html'
    ordering = ['created']

    def get_queryset(self):
        return Book.objects.filter(created_by=self.request.user).values('pk', 'name')
    #def get_queryset(self):
    #    queryset = super().get_queryset()
    #    return queryset.filter(created_by=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object_list
        context['total_books'] = Book.objects.count()
        context['average_price'] = Book.objects.aggregate(Avg('price')).get('price__avg', 0)
        context['price_max'] = Book.objects.aggregate(Max('price')).get('price__max', 0)
        context['price_min'] = Book.objects.aggregate(Min('price')).get('price__min', 0)
        context['books_publisher'] = Book.objects.filter(publisher__name='Rama').count()
        context['books_rama'] = Book.objects.all().filter(publisher__name='Rama')
        context['dif_price'] = Book.objects.aggregate(
            price_diff=Max('price', output_field=FloatField()) - Avg('price')).get('price_diff', 0)
        return context


class BookDetailView(LoginRequiredMixin, DetailView):
    queryset = Book.objects.prefetch_related('authors').select_related('publisher').select_related('created_by')
    template_name = 'book/detail-book.html'
    context_object_name = 'book'

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            return queryset.filter(is_published=True, created_by=self.request.user)
        else:
            return Book.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['n_author'] = self.object.authors.count()
        context['author_name'] = ','.join(self.object.authors.values_list('name', flat=True))
        context['book_publisher'] = self.object.stores.count()
        context['stores'] = Store.objects.filter(books__name=self.object.name)
        return context


class BookCreateView(LoginRequiredMixin, CreateView):
    # If your list page’s queryset doesn’t need any filtering
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

    # Assume we want to populate form’s title field with some initial data.
    def get_initial(self, *args, **kwargs):
        initial = super(BookCreateView, self).get_initial(**kwargs)
        initial['gender'] = 'Pelea'
        return initial


class BookUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Book
    form_class = BookModelForm
    template_name = 'book/update-book.html'
    success_url = reverse_lazy('list_book')

    def test_func(self):
        obj = self.get_object()
        return obj.created_by == self.request.user

    def form_valid(self, form):
        #print(form.cleaned_data)
        book = form.save(commit=False)
        book.created_by = self.request.user
        book.save()
        return super(BookUpdateView, self).form_valid(form)


class BookDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'book/delete-book.html'
    context_object_name = 'book'

    def get_object(self, queryset=None):
        return get_object_or_404(Book, pk=self.kwargs['pk'])

    def get_success_url(self):
        return reverse_lazy('list_book')


class StudentListView(ListView):
    model = Student
    template_name = 'student/list-student.html'
    context_object_name = 'students'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['student_greater'] = Student.objects.student_greater()
        context['student_smaller'] = Student.objects.student_smaller()
        return context


class StudentDetailView(LoginRequiredMixin, DetailView):
    queryset = Student.objects.select_related('university')
    #queryset = Student.objects.select_related()
    template_name = 'student/detail-student.html'
    context_object_name = 'student'


class StudentCreateView(LoginRequiredMixin, CreateView):
    model = Student
    fields = ('first_name', 'last_name', 'university', 'marital_status', 'gender', 'address', 'telephone_number', 'additional_data', 'birthday', 'image')
    template_name = 'student/create-student.html'
    success_url = reverse_lazy('list_student')


class StudentUpdateView(LoginRequiredMixin, UpdateView):
    queryset = Student.objects.select_related('university')
    fields = ('first_name', 'last_name', 'university', 'marital_status', 'gender', 'address', 'telephone_number', 'additional_data', 'birthday', 'image')
    template_name = 'student/update-student.html'

    def get_success_url(self):
        return reverse_lazy('update_student', kwargs={'pk': self.object.id})


class StudentDeleteView(LoginRequiredMixin, DeleteView):
    model = Student.objects.all()
    template_name = 'student/delete-student.html'
    context_object_name = 'student'
    success_url = reverse_lazy('list_student')


class AuthorListView(ListView):
    # represents the objects, supersedes the value provided for model, is a class attribute with a mutable value
    queryset = Author.objects.all().values('pk', 'name')
    template_name = 'author/list-author.html'
    context_object_name = 'authors'

    #def get_queryset(self):
    #    queryset = super(AuthorListView, self).get_queryset()
    #    return queryset.filter(pk=self.kwargs['author_id'])

    #def get_queryset(self):
    #    name = self.request.GET.get('name')
    #    if name:
    #        queryset = Author.objects.filter(name__icontains=name)
    #    else:
    #        queryset = Author.objects.all()
    #    return queryset


class AuthorDetailView(LoginRequiredMixin, DetailView):
    template_name = 'author/detail-author.html'
    context_object_name = 'author'

    def get_object(self, queryset=None):
        return get_object_or_404(Author, pk=self.kwargs['pk'])

    #def get_object(self):
    #    obj = super().get_object()
    #    # Record the last accessed date
    #    obj.last_accessed = timezone.now()
    #    obj.save()
    #    return obj


class AuthorCreateView(LoginRequiredMixin, CreateView):
    model = Author
    template_name = 'author/create-author.html'
    fields = ('name', 'age', 'salutation', 'email')


class AuthorUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'author/update-author.html'
    fields = ('name', 'age', 'salutation', 'email')

    # def get_object(self):
    #    id_ = self.kwargs.get("pk")
    #    return get_object_or_404(Author, id=id_)

    def get_object(self, queryset=None):
        return get_object_or_404(Author, id=self.kwargs['pk'])

    def get_success_url(self):
        return reverse_lazy('update_author', kwargs={'pk': self.object.id})


class AuthorDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'author/delete-author.html'
    context_object_name = 'author'
    success_url = reverse_lazy('list_author')

    def get_object(self, queryset=None):
        return get_object_or_404(Author, pk=self.kwargs['pk'])


class LoanListView(ListView):
    queryset = Loan.objects.all().values('pk', 'order_number')
    template_name = 'loan/list-loan.html'
    context_object_name = 'loans'


class LoanDetailView(LoginRequiredMixin, DetailView):
    queryset = Loan.objects.prefetch_related('book').select_related('student')
    template_name = 'loan/detail-loan.html'
    context_object_name = 'loan'


class LoanCreateView(LoginRequiredMixin, CreateView):
    model = Loan
    template_name = 'loan/create-loan.html'
    fields = ('order_number', 'book', 'student', 'date_s', 'date_e', 'date_d')
    success_url = reverse_lazy('create_loan')


class LoanUpdateView(LoginRequiredMixin, UpdateView):
    queryset = Loan.objects.all()
    template_name = 'loan/update-loan.html'
    fields = ('order_number', 'book', 'student', 'date_s', 'date_e', 'date_d')

    def get_success_url(self):
        return reverse_lazy('update_loan', args=[self.object.pk])


class LoanDeleteView(LoginRequiredMixin, DeleteView):
    model = Loan
    template_name = 'loan/delete-loan.html'
    context_object_name = 'loan'
    success_url = reverse_lazy('list_loan')


class PublisherListView(ListView):
    queryset = Publisher.objects.all().values('pk', 'name')
    template_name = 'publisher/list-publisher.html'
    context_object_name = 'publishers'


class PublisherDetailView(LoginRequiredMixin, DetailView):
    template_name = 'publisher/detail-publisher.html'
    context_object_name = 'publisher'

    def get_object(self, queryset=None):
        return get_object_or_404(Publisher, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book_list'] = self.get_object().books.all()
        context['num_book'] = self.object.books.all().count()
        return context


class PublisherCreateView(LoginRequiredMixin, CreateView):
    model = Publisher
    template_name = 'publisher/create-publisher.html'
    fields = ('name', 'address', 'city', 'state_province', 'country', 'website')
    success_url = reverse_lazy('create_publisher')


class PublisherUpdateView(LoginRequiredMixin, UpdateView):
    model = Publisher
    template_name = 'publisher/update-publisher.html'
    fields = ('name', 'address', 'city', 'state_province', 'country', 'website')

    def get_success_url(self):
        return reverse_lazy('update_publisher', args=[self.object.pk])


class PublisherDeleteView(LoginRequiredMixin, DeleteView):
    model = Publisher
    template_name = 'publisher/delete-publisher.html'
    context_object_name = 'publisher'
    success_url = reverse_lazy('list_publisher')
