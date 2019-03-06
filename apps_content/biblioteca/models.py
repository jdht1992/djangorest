from django.db import models
from model_utils.models import TimeStampedModel
from model_utils import Choices
from django.conf import settings
from apps_content.users.models import CustomUser


class Author(TimeStampedModel):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    salutation = models.CharField(max_length=150)
    email = models.EmailField()

    def __str__(self):
        return f"{self.id} - {self.name}"


class Publisher(TimeStampedModel):
    name = models.CharField(max_length=300)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

    class Meta:
        ordering = ["-pk"]

    def __str__(self):
        return f"{self.pk} - {self.name}"


class Book(TimeStampedModel):
    name = models.CharField(max_length=300)
    book_code = models.CharField(max_length=300)
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)#para almacenar números hasta 999 con una resolución de 2 decimales
    rating = models.FloatField()
    authors = models.ManyToManyField(Author, related_name="book", blank=True, null=True)
    publisher = models.ForeignKey(Publisher, related_name="book", on_delete=models.CASCADE)
    publication_date = models.DateField()
    gender = models.CharField(max_length=300)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='book')

    def __str__(self):
        return f"{self.pk} - {self.name}"


class Store(TimeStampedModel):
    name = models.CharField(max_length=100)
    direction = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)

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
    university_type = models.CharField(choices=UNIVERSITY_TYPE, default=UNIVERSITY_TYPE, max_length=100,)

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
    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name='university')
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

    class Meta:  # new
        verbose_name = 'student'
        verbose_name_plural = 'students'

    def __str__(self):
        return f"{self.first_name}"


class Loan(TimeStampedModel):
    order_number = models.CharField(max_length=300)
    book = models.ManyToManyField(Book, related_name='loan')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='loan')
    date_s = models.DateField()
    date_e = models.DateField()
    date_d = models.DateField()

    def __str__(self):
        return self.order_number

