from django.contrib import admin
from . import models
from affects import models as affects_models

@admin.register(models.Movie)
class ModelAdmin(admin.ModelAdmin):
    """ Room Admin Definition """

    list_display = (
        "title",
        "script",
    )
    
    filter_horizontal = ("affect",)