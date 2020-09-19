from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.

class Celebrity(models.Model):
    name = models.CharField(max_length = 64,verbose_name = '이름')
    birth = models.DateField(verbose_name = '생년월일')
    job = models.CharField(max_length = 64, verbose_name = '직업')
    edu = models.CharField(max_length = 256, verbose_name = '학력')
    photo = models.ImageField(upload_to = '%d')

    visitor_today = models.IntegerField(default = 0, verbose_name = '오늘 방문자')
    visitor_total = models.IntegerField(default = 0, verbose_name = '총 방문자')

    def visitor(self):
        pass