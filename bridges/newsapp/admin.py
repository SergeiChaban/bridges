from django.contrib import admin
from .models import *


class NewsImageInline(admin.TabularInline):
    model = NewsImage
    extra = 0

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)
    inlines = [
        NewsImageInline,
    ]
