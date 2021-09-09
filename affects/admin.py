from django.contrib import admin
from . import models

@admin.register(models.Affect)
class AffectAdmin(admin.ModelAdmin):
    """ Room Admin Definition """

    list_display = (
        "affect_kr",
        "description",
        "definition",
    )