from django.contrib import admin
from .models import AppUser

class AppUserAdmin(admin.ModelAdmin):
    list_display = ("id", "email", "name", "phone", "role", "is_active", "is_staff")
    search_fields = ("email", "name")

admin.site.register(AppUser, AppUserAdmin)
