from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe
from import_export.admin import ExportActionModelAdmin, ImportExportMixin, ImportMixin

# Register your models here.

class DisplayCelebrity(ImportExportMixin, admin.ModelAdmin):
    list_display = ('name', 'job', 'birth', 'edu', 'photo', 'get_image')

    def get_image(self, obj):
        return mark_safe('<img src="{url}" width="{width} height ="{height}"/>'.format(
            url = obj.photo.url,
            width = 200,
            height = 200,
        ))

admin.site.register(Celebrity, DisplayCelebrity)
