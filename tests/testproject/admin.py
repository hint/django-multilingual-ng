from django.contrib import admin
from multilingual.admin import MultilingualModelAdmin, MultilingualInlineAdmin
from models import MultiModel,MultiModel2, MultiInlineModel


class MultiModelAdmin(MultilingualModelAdmin):
    
    list_display = ('field1', 'field2', 'field3',)
    ordering = ['-field3']

class MultiInlineAdmin(MultilingualInlineAdmin):
   model = MultiInlineModel 

class MultiModel2Admin(MultilingualModelAdmin):
    inlines = (MultiInlineAdmin,)

admin.site.register(MultiModel, MultiModelAdmin)
admin.site.register(MultiModel2, MultiModel2Admin)
