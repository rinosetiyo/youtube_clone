from django.urls import path
from youtubeClone import views

urlpatterns = [
    path('', views.index, name="index"),
]
