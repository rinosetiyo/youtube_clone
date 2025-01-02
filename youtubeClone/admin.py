from django.contrib import admin
from youtubeClone.models import Video, Comment
from import_export.admin import ImportExportModelAdmin

# Register your models here.
class VideoAdmin(ImportExportModelAdmin):
    pass

admin.site.register(Video, VideoAdmin)
admin.site.register(Comment)