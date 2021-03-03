from django.contrib import admin
from .models import MyUser
from .forms import MyUserCreationForm
from django.contrib.auth.admin import UserAdmin

class CustomAdmin(UserAdmin):
    model = MyUser
    add_form = MyUserCreationForm

    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Información Cliente',
            {
                'fields': (
            'pais',
            'telefono',
                )
            }
        )
    )
        

admin.site.register(MyUser, CustomAdmin)