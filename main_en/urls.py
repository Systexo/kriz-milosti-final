# main_en/urls.py
from django.urls import path
from . import views

app_name = "main_en"

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("visit-us/", views.visit_us, name="visit_us"),
    path("sermons/", views.sermons, name="sermons"),
    path("connect/", views.connect, name="connect"),
    path("statement-of-faith/", views.statement_of_faith, name="statement_of_faith"),
]
