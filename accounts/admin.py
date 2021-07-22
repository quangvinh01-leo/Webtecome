from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account

# Register your models here.

class AccountAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name','username','last_login','date_joinned','is_active')
    list_display_link = ('email', 'first_name', 'last_name')
    readonly_fields = ('last_login','date_joinned')
    ordering = ('-date_joinned',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Account,AccountAdmin)