from django.contrib import admin
from .models import UserAccount


@admin.register(UserAccount)
class UserAdmin(admin.ModelAdmin):

    list_display = ("id","name", "email")
    list_filter = ("name", "email")