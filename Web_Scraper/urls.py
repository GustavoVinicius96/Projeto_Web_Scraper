from django.urls import path

from . import views

app_main = "Projeto_Final"

urlpatterns = [
    path("", views.homepage, name="homepage"),
]
