from django.contrib import admin
from .models import CategoryCompany, FormCompany, Company, Users, CompanyUsers


class CompanyUsersInline(admin.TabularInline):
    model = CompanyUsers
    extra = 0


@admin.register(CategoryCompany)
class CategoryCompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description',)


@admin.register(FormCompany)
class FormCompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description',)


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'inn', 'category', 'city')
    search_fields = ('name', 'inn', )
    # укажем быстрые фильтры для фильтрации записей
    list_filter = ('category', 'city')


@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    # поля, которые не нужно редактировать в админке
    readonly_fields = ('password', 'is_superuser', 'last_login', 'date_joined')  # 'user_permissions', 'groups')

    # какие поля выводить в админке
    list_display = ('username', 'first_name', 'last_name', 'is_active', 'is_staff', 'phone', 'email')

    # по каким полям может осуществляться поиск в админке
    search_fields = ('username',
                     'first_name',
                     'last_name',
                     'patronymic',
                     'phone',
                     'email',)

    # укажем быстрые фильтры для фильтрации записей
    list_filter = ('is_staff', 'is_active', 'gender')

    # в админке поля формы можно группировать
    fieldsets = (
        ('Личные данные',
         {'fields': ('username', 'password', 'first_name', 'last_name', 'patronymic', 'gender', 'birthday')}),
        ('Контактные данные', {'fields': ('phone', 'email')}),
        ('Данные сотрудника',
         {'fields': ('is_staff', 'is_active', 'groups',)}),
    )
    inlines = [
        CompanyUsersInline,
    ]
