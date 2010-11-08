from django.db import models
from multilingual.manager import MultilingualManager
from multilingual.translation import TranslationModel


class MultiModel(models.Model):
    
    """
    This is an example model that has both translated and non-translated fields.
    """
    
    field1 = models.CharField(max_length=50)
    
    objects = MultilingualManager()
    
    class Translation(TranslationModel):
        
        field2 = models.CharField(max_length=50)
        field3 = models.IntegerField() 
        
        class Meta:
            ordering = ['field2']
            
    def __unicode__(self):
        return self.field1