# Generated by Django 3.1.4 on 2021-01-03 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210103_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='links',
            field=models.TextField(verbose_name='Список ссылок'),
        ),
    ]
