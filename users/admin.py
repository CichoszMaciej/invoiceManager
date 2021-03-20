from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import Employee


class EmployeeAdmin(UserAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'date_joined', 'last_login', 'is_admin', 'is_staff')
    search_fields = ('username', 'email',)
    readonly_fields = ('date_joined', 'last_login',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'email'),
        }),
    )


admin.site.register(Employee, EmployeeAdmin)
