# Generated by Django 2.1.7 on 2019-03-28 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0026_auto_20190322_0036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='university',
            name='university_type',
            field=models.CharField(choices=[('Public', 'A public university'), ('Private', 'A private university')], default='Public', max_length=30),
        ),
    ]