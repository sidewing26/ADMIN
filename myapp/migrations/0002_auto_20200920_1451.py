# Generated by Django 3.1.1 on 2020-09-20 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='celebrity',
            name='visited_day',
            field=models.DateField(blank=True, null=True, verbose_name='방문일자'),
        ),
    ]
