from django.contrib import admin
from .models import Resume
from django.contrib import admin
from parser_app.models import UserProfileInfo, User
# Register your models here

admin.site.register(UserProfileInfo)

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    pass