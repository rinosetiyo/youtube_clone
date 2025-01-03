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
    cover_image = models.ImageField(upload_to=channel_directory_path, null=True)
    images = models.ImageField(upload_to=channel_directory_path, null=True)
    full_name = models.CharField(max_length=100)
    channel_name = models.CharField(max_length=200)
    description = models.TextField()
    keywords = TaggableManager()
    joined = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=STATUS, max_length=100, default='active')
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, related_name="channel")
    subscribers = models.ManyToManyField(User, related_name="user_subs", null=True, blank=True)
    verified = models.BooleanField(default=False)

    # business account
    email_business = models.EmailField(null=True, blank=True)
    make_email_public = models.BooleanField(default=False)

    # location
    location_business = models.CharField(max_length=200, null=True, blank=True)
    make_location_public = models.BooleanField(default=False)

    # social media links
    social_media_links = models.CharField(max_length=200, null=True, blank=True, default="https://www.youtube.com/")
    social_media_links2 = models.CharField(max_length=200, null=True, blank=True)
    social_media_links3 = models.CharField(max_length=200, null=True, blank=True)
    social_media_links4 = models.CharField(max_length=200, null=True, blank=True)
    make_social_media_public = models.BooleanField(default=False)

    def __str__(self):
        return self.channel_name
    
class Community(models.Model):
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=channel_directory_path, null=True)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100, choices=STATUS, default="active")
    likes = models.ManyToManyField(User)

    def __str__(self):
        return self.channel_name
    
    class meta:
        verbose_name_plural = 'Communities'

class CommunityComment(models.Model):
    community = models.ForeignKey(Community, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100, choices=STATUS, default="active")

    def __str__(self):
        return self.comment
    
    class meta:
        verbose_name_plural = 'Community Comments'