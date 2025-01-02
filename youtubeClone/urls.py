from django.urls import path
from youtubeClone import views

urlpatterns = [
    path('', views.index, name="index"),
    path("<video_id>/", views.video_detail, name="video_detail"),
]
