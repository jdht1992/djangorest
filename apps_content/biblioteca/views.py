from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, ListView, TemplateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django import forms
from django.db.models import Avg, Max, Min, FloatField

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


class UniversityDeleteView(DeleteView):
    template_name = 'university/delete-university.html'
    context_object_name = 'university'

    def get_object(self, queryset=None):
        return get_object_or_404(University, pk=self.kwargs['pk'])

    def get_success_url(self):
        return reverse_lazy('list_university')


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


class StoreDeleteView(DeleteView):
    template_name = 'store/delete-store.html'
    context_object_name = 'store'

    def get_object(self, queryset=None):
        return get_object_or_404(Store, pk=self.kwargs['pk'])

    def get_success_url(self):
        return reverse_lazy('list_store')


class BookListView(ListView):
    template_name = 'book/list-book.html'
    context_object_name = 'books'

    def get_queryset(self):
        return Book.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_books'] = Book.objects.count()
        context['average_price'] = Book.objects.aggregate(Avg('price')).get('price__avg', 0)
        context['price_max'] = Book.objects.aggregate(Max('price')).get('price__max', 0)
        context['price_min'] = Book.objects.aggregate(Min('price')).get('price__min', 0)
        context['books_publisher'] = Book.objects.filter(publisher__name='Rama').count()
        context['books_rama'] = Book.objects.all().filter(publisher__name='Rama')
        context['dif_precio'] = Book.objects.aggregate(
            price_diff=Max('price', output_field=FloatField()) - Avg('price')).get('price_diff', 0)
        return context


class BookDetailView(DetailView):
    template_name = 'book/detail-book.html'
    context_object_name = 'book'

    def get_object(self, queryset=None):
        return get_object_or_404(Book, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # book = Book.objects.first()
        context['n_author'] = self.get_object().authors.count()
        context['authro_name'] = ','.join(self.get_object().authors.values_list('name', flat=True))
        context['book_publisher'] = self.get_object().store_set.count()
        context['stores'] = Store.objects.filter(books__name=self.object.name)
        return context


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
        #print(form.cleaned_data)
        book = form.save(commit=False)
        book.created_by = self.request.user
        book.save()
        return super(BookUpdateView, self).form_valid(form)


class BookDeleteView(DeleteView):
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


class StudentDeleteView(DeleteView):
    template_name = 'student/delete-student.html'
    context_object_name = 'student'

    def get_object(self, queryset=None):
        return get_object_or_404(Student, pk=self.kwargs['pk'])

    def get_success_url(self):
        return reverse_lazy('list_student')


class AuthorListView(ListView):
    template_name = 'author/list-author.html'
    context_object_name = 'authors'

    def get_queryset(self):
        return Author.objects.all()

    #def get_queryset(self):
    #    name = self.request.GET.get('name')
    #    if name:
    #        queryset = Author.objects.filter(name__icontains=name)
    #    else:
    #        queryset = Author.objects.all()
    #    return queryset


class AuthorDetailView(DetailView):
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


class AuthorCreateView(CreateView):
    model = Author
    template_name = 'author/create-author.html'
    fields = ('name', 'age', 'salutation', 'email')

#    def get_success_url(self):
#        return reverse_lazy('create_author')


class AuthorUpdateView(UpdateView):
    model = Author
    template_name = 'author/update-author.html'
    fields = ('name', 'age', 'salutation', 'email')
    success_url = reverse_lazy('list_author')

    # def get_object(self):
    #    id_ = self.kwargs.get("pk")
    #    return get_object_or_404(Author, id=id_)

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book_list'] = self.get_object().books.all()
        context['num_book'] = self.get_object().books.all().count()
        return context


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


"""
class CreateUser(FormView):
    template_name='usuario/nuevo-user.html'
    form_class=CreateUserModelForm

    def get_success_url(self):
        return reverse('nuevo_user')

    def post(self, request, *args, **kwargs):
        form=self.get_form()
        u=User.objects.create_user(
            form.cleaned_data['username'],
            form.cleaned_data['email'],
            form.cleaned_data['password']
        )
        u.last_name=form.cleaned_data['last_name']
        u.save()
        return self.form_valid(form)
"""