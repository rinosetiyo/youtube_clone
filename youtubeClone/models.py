from django.db import models
from statistics import mode
from taggit.managers import TaggableManager
from django.conf import settings

# Create your models here.
User = settings.AUTH_USER_MODEL

def user_directory_path(instance, filename):
    return f'videos/user_{instance.user.id}/{filename}'

def thumbnail_directory_path(instance, filename):
    return f'thumbnails/user_{instance.user.id}/{filename}'

VISIBILITY = (
    ('public', 'Public'),
    ('private', 'Private'),
    ('unlisted', 'Unlisted'),
    ('member_only', 'Member Only')
)

class Video(models.Model):
    video = models.FileField(upload_to=user_directory_path, null=True)
    thumbnail = models.ImageField(upload_to=thumbnail_directory_path, null=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    tags = TaggableManager()
    visibility = models.CharField(choices=VISIBILITY, max_length=100, default='public')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    views = models.PositiveIntegerField(default=0)
    likes = models.ManyToManyField(User, related_name='video_likes')

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment