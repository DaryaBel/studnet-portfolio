# Generated by Django 3.1.4 on 2021-01-12 19:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_remove_students_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='universities',
            name='phone',
        ),
    ]
