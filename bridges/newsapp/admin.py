from django.contrib import admin
from .models import *

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)
    inlines = [
    ]
