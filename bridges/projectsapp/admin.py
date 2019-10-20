from django.contrib import admin

from .models import *


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 0


class ProjectHasTechnicalSolutionsInline(admin.TabularInline):
    model = ProjectHasTechnicalSolutions
    extra = 0


class ProjectCompanyInline(admin.TabularInline):
    model = ProjectCompany
    extra = 0


class ProjectManagersInline(admin.TabularInline):
    model = ProjectManagers
    extra = 0
    # fields = ('role', 'manager', 'is_active', 'description',)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'city',)
    list_display_links = ('name', 'city',)
    search_fields = ('name',)
    exclude = ['map_mark']
    inlines = [
        ProjectManagersInline,
        ProjectCompanyInline,
        ProjectHasTechnicalSolutionsInline,
        ProjectImageInline
    ]


@admin.register(ProjectHasTechnicalSolutions)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)


@admin.register(ProjectManagers)
class ProjectManagersAdmin(admin.ModelAdmin):
    list_display = ('manager',)
    list_display_links = ('manager',)
