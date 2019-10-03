from django.contrib import admin
from .models import *


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 0


class ProjectHasTechnicalSolutionsInline(admin.TabularInline):
    model = ProjectHasTechnicalSolutions
    extra = 0


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'city',)
    list_display_links = ('name', 'city',)
    search_fields = ('name',)
    inlines = [
        ProjectHasTechnicalSolutionsInline,
        ProjectImageInline,
    ]


@admin.register(ProjectHasTechnicalSolutions)
class ProjectHasTechnicalSolutionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'value', 'created', 'updated',)
    list_display_links = ('id', 'value',)


@admin.register(ProjectImage)
class ProjectImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'is_active', 'created', 'updated',)
    list_display_links = ('id', 'image',)



