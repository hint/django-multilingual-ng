from django.contrib import admin
from multilingual.admin import MultilingualModelAdmin
from models import MultiModel


class MultiModelAdmin(MultilingualModelAdmin):
    
    list_display = ('field1', 'field2', 'field3',)
    ordering = ['-field3']


admin.site.register(MultiModel, MultiModelAdmin)