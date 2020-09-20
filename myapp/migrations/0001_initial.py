# Generated by Django 3.1.1 on 2020-09-20 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Celebrity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='이름')),
                ('birth', models.DateField(verbose_name='생년월일')),
                ('job', models.CharField(max_length=64, verbose_name='직업')),
                ('edu', models.CharField(max_length=256, verbose_name='학력')),
                ('photo', models.ImageField(upload_to='%d')),
                ('visitor_today', models.IntegerField(default=0, verbose_name='오늘 방문자')),
                ('visitor_total', models.IntegerField(default=0, verbose_name='총 방문자')),
                ('visited_day', models.DateField(blank=True, verbose_name='방문일자')),
            ],
        ),
    ]
