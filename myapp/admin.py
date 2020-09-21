from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe
from import_export.admin import ExportActionModelAdmin, ImportExportMixin, ImportMixin

# Register your models here.

class DisplayCelebrity(ImportExportMixin, admin.ModelAdmin):
    list_display = ('name', 'job', 'birth', 'edu', 'get_image')
    search_fields = ('name', 'job')
    list_filter = ('job',)

    def get_image(self, obj):
        return mark_safe('<img src="{url}" width="{width} height ="{height}"/>'.format(
            url = obj.photo.url,
            width = 150,
            height = 150,
        ))

admin.site.register(Celebrity, DisplayCelebrity)
