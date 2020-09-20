from django.db import models
from datetime import datetime

# Create your models here.

class Celebrity(models.Model):
    name = models.CharField(max_length = 64,verbose_name = '이름')
    birth = models.DateField(verbose_name = '생년월일')
    job = models.CharField(max_length = 64, verbose_name = '직업')
    edu = models.CharField(max_length = 256, verbose_name = '학력')
    photo = models.ImageField(upload_to = '%d')

    visitor_today = models.IntegerField(default = 0, verbose_name = '오늘 방문자')
    visitor_total = models.IntegerField(default = 0, verbose_name = '총 방문자')
    visited_day = models.TextField(blank = True, null = True, verbose_name = '방문일자')

    @property
    def visitor(self):
        today = datetime.today().strftime("%Y-%m-%d")
        if self.visited_day == today:
            self.visitor_today += 1
            self.visitor_total += 1
            self.save()

        else:
            self.visited_day = today
            self.visitor_today = 0
            self.visitor_today += 1
            self.visitor_total += 1
            self.save()
