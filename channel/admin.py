from django.contrib import admin
from channel.models import Channel, Community, CommunityComment
from import_export.admin import ImportExportModelAdmin

# Register your models here.
admin.site.register(Channel)