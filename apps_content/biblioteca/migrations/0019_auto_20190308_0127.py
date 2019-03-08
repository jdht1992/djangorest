# Generated by Django 2.1.7 on 2019-03-08 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0018_auto_20190307_2338'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='file_book',
            field=models.FileField(default='nada.png', upload_to='file_book'),
        ),
        migrations.AlterField(
            model_name='university',
            name='university_type',
            field=models.CharField(choices=[('Public', 'A public university'), ('Private', 'A private university')], default=(('Public', 'A public university'), ('Private', 'A private university')), max_length=100),
        ),
    ]
