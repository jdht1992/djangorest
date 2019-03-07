# Generated by Django 2.1.7 on 2019-03-07 20:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0014_auto_20190307_2009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='biblioteca.Publisher'),
        ),
        migrations.AlterField(
            model_name='university',
            name='university_type',
            field=models.CharField(choices=[('Public', 'A public university'), ('Private', 'A private university')], default=(('Public', 'A public university'), ('Private', 'A private university')), max_length=100),
        ),
    ]