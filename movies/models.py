from django.db import models
from core import models as core_models
from affects import models as affects_models


class Movie(core_models.TimeStampedModel):
    
    title = models.CharField(max_length=200)
    original_title = models.CharField(max_length=200, blank=True, null=True)
    info = models.URLField()
    script = models.TextField()
    video = models.URLField()
    
    netflix_link = models.URLField(blank=True, null=True)
    wavve_link = models.URLField(blank=True, null=True)
    tving_link = models.URLField(blank=True, null=True)
    watcha_link = models.URLField(blank=True, null=True)
    
    affect = models.ManyToManyField(affects_models.Affect, blank=True)
    
    twitter = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return self.title
