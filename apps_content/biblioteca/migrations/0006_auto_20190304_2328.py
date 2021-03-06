# Generated by Django 2.1.7 on 2019-03-04 23:28

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0005_auto_20190304_2327'),
    ]

    operations = [
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('order_number', models.CharField(max_length=300)),
                ('date_s', models.DateField()),
                ('date_e', models.DateField()),
                ('date_d', models.DateField()),
                ('book', models.ManyToManyField(related_name='loan', to='biblioteca.Book')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loan', to='biblioteca.Student')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='university',
            name='university_type',
            field=models.CharField(choices=[('Public', 'A public university'), ('Private', 'A private university')], default=(('Public', 'A public university'), ('Private', 'A private university')), max_length=100),
        ),
    ]
