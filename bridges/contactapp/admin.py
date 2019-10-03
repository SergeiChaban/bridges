from django.contrib import admin
from contactapp.models import ContactApplication


class ContactFormAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'add_datetime',)
    list_display_links = ('name',)
    search_fields = ('name', 'subject', 'phone',)

    class Meta:
        model = ContactApplication


admin.site.register(ContactApplication, ContactFormAdmin)
