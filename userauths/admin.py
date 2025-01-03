from django.contrib import admin
from userauths.models import User, Profile
from import_export.admin import ImportExportModelAdmin

# Register your models here.
class UserAdmin(ImportExportModelAdmin):
    pass

admin.site.register(User, UserAdmin)
admin.site.register(Profile)