from django.db import models
from statistics import mode
from taggit.managers import TaggableManager
from django.conf import settings

# Create your models here.
User = settings.AUTH_USER_MODEL

STATUS = (
    ('active', 'Active'),
    ('disable', 'Disable'),
)

def channel_directory_path(instance, filename):
    return f'thumbnails/user_{instance.user.id}/{filename}'

class Channel(models.Model):
    images = models.ImageField(upload_to=channel_directory_path, null=True)
    full_name = models.CharField(max_length=100)
    channel_name = models.CharField(max_length=200)
    description = models.TextField()
    keywords = TaggableManager()
    joined = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=STATUS, max_length=100, default='public')
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, related_name="channel")
    subscribers = models.ManyToManyField(User, related_name="user_subs")
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.channel_name