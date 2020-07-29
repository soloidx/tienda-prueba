from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Usuario

# Register your models here.
#


class UserAdmin(BaseUserAdmin):
    fieldsets = BaseUserAdmin.fieldsets + (
        (
            "Datos adicionales",
            {
                "fields": (
                    "tipo_documento",
                    "numero_documento",
                    "direccion",
                    "referencia",
                    "celular",
                )
            },
        ),
    )


admin.site.register(Usuario, UserAdmin)
