# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import *

class NewsHasTechnicalSolutionsInline(admin.TabularInline):
    model = NewsHasTechnicalSolutions
    extra = 0

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)
    inlines = [
        NewsHasTechnicalSolutionsInline
    ]
