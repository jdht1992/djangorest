from django.db import models

# Create your models here.

class Contact(models.Model):
    from_email = models.EmailField()
    subject = models.CharField(max_length=50)
    message = models.TextField(max_length=50)

    def __str__(self):
        return self.subject
