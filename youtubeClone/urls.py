from django.urls import path
from youtubeClone import views

urlpatterns = [
    path('', views.index, name="index"),
    path("videos/<video_id>/", views.video_detail, name="video_detail"),
    path("channel/<channel_id>", views.channel_view, name="channel_view"),
    path("test/", views.test, name="test"),
]
