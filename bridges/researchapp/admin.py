from django.contrib import admin


# Register your models here.
from researchapp.models import Document, FileStorage, SubjectOfStudy, DocumentCategory


class SubjectOfStudyInline(admin.TabularInline):
    model = SubjectOfStudy
    extra = 1


class FileStorageInline(admin.TabularInline):
    model = FileStorage
    extra = 1


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'date')
    list_display_links = ('name',)
    search_fields = ('name',)


@admin.register(SubjectOfStudy)
class SubjectOfStudyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description',)
    list_display_links = ('id', 'name',)


@admin.register(DocumentCategory)
class DocumentCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'comment',)
    list_display_links = ('id', 'name',)


@admin.register(FileStorage)
class FileStorageAdmin(admin.ModelAdmin):
    list_display = ('id', 'alt_desc', 'file', 'is_active', 'created', 'updated',)
    list_display_links = ('id', 'alt_desc',)
