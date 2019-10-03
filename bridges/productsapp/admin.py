from django.contrib import admin
from .models import *


class MaterialCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name', )

    class Meta:
        model = MaterialCategory


admin.site.register(MaterialCategory, MaterialCategoryAdmin)


class MeasureTypesAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)

    class Meta:
        model = MeasureTypes


admin.site.register(MeasureTypes, MeasureTypesAdmin)


class MaterialImageInline(admin.TabularInline):
    model = MaterialImage
    extra = 0


class MaterialAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'category', 'measure',)
    list_display_links = ('name',)
    search_fields = ('name',)
    inlines = [MaterialImageInline]

    class Meta:
        model = Material


admin.site.register(Material, MaterialAdmin)


class MaterialImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'is_active', 'created', 'updated',)
    list_display_links = ('id', 'image',)

    class Meta:
        model = MaterialImage


admin.site.register(MaterialImage, MaterialImageAdmin)


class TechnicalSolutionsImageInline(admin.TabularInline):
    model = TechnicalSolutionsImage
    extra = 0


class TechnicalSolutionsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', )
    list_display_links = ('name',)
    search_fields = ('name',)
    inlines = [TechnicalSolutionsImageInline]

    class Meta:
        model = TechnicalSolutions


admin.site.register(TechnicalSolutions, TechnicalSolutionsAdmin)


class TechnicalSolutionsImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'is_active', 'created', 'updated',)
    list_display_links = ('id', 'image',)

    class Meta:
        model = TechnicalSolutionsImage


admin.site.register(TechnicalSolutionsImage, TechnicalSolutionsImageAdmin)