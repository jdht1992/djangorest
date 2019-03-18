from django.db import models
from model_utils.models import TimeStampedModel
from model_utils import Choices
from django.conf import settings
from apps_content.users.models import CustomUser
from django.urls import reverse


class Author(TimeStampedModel):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    salutation = models.CharField(max_length=150)
    email = models.EmailField()

    def __str__(self):
        return f"{self.id} - {self.name}"

    def get_absolute_url(self):
        return reverse('detail_author', args=[str(self.id)])


class Publisher(TimeStampedModel):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

    class Meta:
        ordering = ["-pk"]

    def __str__(self):
        return f"{self.pk} - {self.name}"

    def get_absolute_url(self):
        return reverse('detail_author', kwargs={'pk': self.id})


class Book(TimeStampedModel):
    name = models.CharField(max_length=50)
    book_code = models.CharField(max_length=50)
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)#para almacenar números hasta 999 con una resolución de 2 decimales
    rating = models.FloatField()
    authors = models.ManyToManyField(Author, related_name="books", related_query_name='book', blank=True)
    publisher = models.ForeignKey(Publisher, related_name="books", related_query_name='book', on_delete=models.CASCADE)
    publication_date = models.DateField()
    gender = models.CharField(max_length=50)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='book')
    file_book = models.FileField(upload_to='file_book', default='nada.png')

    def __str__(self):
        return f"{self.pk} - {self.name}"

    #def save(self, *args, **kwargs):
    #    self.created_by =
    #    super(Book, self).save(*args, **kwargs)

#    def __init__(self, *args, **kwargs):
#        self.request = kwargs.pop('request', None)
#        self.created_by = self.request.user.email
#        super(Book, self).__init__(*args, **kwargs)


class Store(TimeStampedModel):
    # Cuando no tiene relacion puede configurarlo como un primer argumento opcional el name.
    name = models.CharField('Name', max_length=100)
    # O bien puesdes usar verbose_name
    direction = models.CharField(verbose_name='Direction', max_length=100)
    books = models.ManyToManyField(Book, related_name='stores', related_query_name='store')

    def __str__(self):
        return self.name


class University(TimeStampedModel):
    full_name = models.CharField(max_length=150)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=150)
    UNIVERSITY_TYPE = Choices(
        #se almacena - se muestra en pantalla
        ('Public', 'A public university'),
        ('Private', 'A private university')
    )
    university_type = models.CharField(choices=UNIVERSITY_TYPE, default=UNIVERSITY_TYPE, max_length=100)

    class Meta:
        indexes = [models.Index(fields=['full_name'])]
        ordering = ['full_name']
        verbose_name = 'university'
        verbose_name_plural = 'universities'

    def __str__(self):
        return f"{self.pk} - {self.full_name}"


class Student(TimeStampedModel):
    # blank = False, null=False se requiere un valor.
    first_name = models.CharField('first name', max_length=30, blank=False, null=False, help_text='Nombre verdadero')
    # blank=True, null=True entonces un formulario permitirá un valor vacío
    last_name = models.CharField('last name', max_length=30, blank=True, null=True)
    # related_name () debe ser el plural del modelo que contiene ForeignKey, related_query_name () debe ser singular.
    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name='students', related_query_name='student')
    MARITAL_STATUS = (
        ('Single', 'Single'),
        ('Merried', 'Merried'),
        ('Divorced', 'Divorced'),
        ('Separated', 'Separated'),
        ('Widow', 'Widow'),
        ('Widower', 'Widower')
    )
    marital_status = models.CharField(choices=MARITAL_STATUS, default=MARITAL_STATUS, max_length=10)
    GENDER = (
        ('Female', 'Female'),
        ('Male', 'Male'),
    )
    gender = models.CharField(choices=GENDER, default=GENDER, max_length=10)
    address = models.CharField(max_length=200)
    telephone_number = models.CharField(max_length=12)
    additional_data = models.TextField(max_length=500, blank=True)
    birthday = models.DateField()
    image = models.ImageField(upload_to='img_student', max_length=50)

    class Meta:  # new
        verbose_name = 'student'
        verbose_name_plural = 'students'

    def __str__(self):
        return f"{self.first_name}"


class Loan(TimeStampedModel):
    order_number = models.CharField(max_length=300)
    book = models.ManyToManyField(Book, related_name='loans', related_query_name='loan')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='loans', related_query_name='loan')
    date_s = models.DateField()
    date_e = models.DateField()
    date_d = models.DateField()

    def __str__(self):
        return self.order_number
