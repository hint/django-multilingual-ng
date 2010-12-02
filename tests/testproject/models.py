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

class MultiModel2(models.Model):

    """
    This is an example model that will be referenced by another model
    """
    
    field1 = models.CharField(max_length=20)
    
    objects = MultilingualManager()
    
    class Translation(TranslationModel):
        field2 = models.CharField(max_length=50)

        class Meta:
            ordering = ['field2']
        
    def __unicode__(self):
        return self.field1

class MultiInlineModel(models.Model):
    
    """
    This is an example model with reference to another model
    """

    ref1 = models.ForeignKey(MultiModel2)

    class Translation(TranslationModel):
        field1 = models.CharField(max_length=50)
