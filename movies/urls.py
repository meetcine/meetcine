from django.urls import path
from . import views

app_name = "movies"

urlpatterns = [
    path("random/", views.RandomView.as_view(), name="random"),
]
