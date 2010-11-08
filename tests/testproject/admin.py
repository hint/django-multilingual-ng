from django.contrib import admin
from multilingual.admin import MultilingualModelAdmin
from models import MultiModel


class MultiModelAdmin(MultilingualModelAdmin):
    
    ordering = ['field3']


admin.site.register(MultiModel, MultiModelAdmin)