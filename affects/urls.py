from django.urls import path
from . import views

app_name = "affects"

urlpatterns = [
    path("a_list/", views.AffectView.as_view(), name="list"),
    path("<int:pk>", views.affect_detail, name="detail"),
]
