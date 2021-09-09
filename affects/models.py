from django.db import models
from core import models as core_models

class Affect(core_models.TimeStampedModel):
    affect_kr = models.CharField(max_length=140)
    affect_en = models.CharField(max_length=140)
    description = models.TextField()
    des_source = models.CharField(max_length=140)
    definition = models.TextField(blank=True, null=True )
    
    def __str__(self):
        return self.affect_kr