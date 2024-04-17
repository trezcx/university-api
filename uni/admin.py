from django.contrib import admin
from .models import University, User

@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name']