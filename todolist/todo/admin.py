from django.contrib import admin
from .models import Todo


@admin.register(Todo)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
