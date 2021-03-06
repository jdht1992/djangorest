# Generated by Django 2.1.7 on 2019-03-05 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0009_auto_20190304_2337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(blank=True, null=True, related_name='book', to='biblioteca.Author'),
        ),
        migrations.AlterField(
            model_name='university',
            name='university_type',
            field=models.CharField(choices=[('Public', 'A public university'), ('Private', 'A private university')], default=(('Public', 'A public university'), ('Private', 'A private university')), max_length=100),
        ),
    ]
