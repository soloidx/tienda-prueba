from django.contrib import admin

from ventas.models import Venta, Producto, DetalleVenta

# Register your models here.


class ProductoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "tipo", "precio")
    list_filter = [
        "tipo",
    ]


class DetalleInline(admin.TabularInline):
    model = DetalleVenta
    extra = 1


class VentaAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "get_tipo_documento",
        "get_numero_documento",
        "total",
        "forma_pago",
        "vuelto",
        "get_direccion",
        "get_referencia",
        "get_celular",
        "fecha_recepcion",
        "fecha_entrega",
    )
    raw_id_fields = ["cliente"]
    inlines = [DetalleInline]
    autocomplete_lookup_fields = {"fk": ["cliente"]}
    search_fields = [
        "cliente__first_name",
        "cliente__last_name",
        "cliente__numero_documento",
    ]

    fieldsets = (
        (None, {"fields": ("cliente", "fecha_entrega")}),
        (
            "Detalle de ventas",
            {
                "classes": ("placeholder", "detalleventa_set-group"),
                "fields": [],
            },
        ),
        ("Resumen", {"fields": ("total", "forma_pago", "vuelto")}),
    )

    def get_tipo_documento(self, obj):
        return obj.cliente.tipo_documento

    get_tipo_documento.short_description = "Tipo de documento"

    def get_numero_documento(self, obj):
        return obj.cliente.numero_documento

    get_numero_documento.short_description = "Numero de documento"

    def get_direccion(self, obj):
        return obj.cliente.direccion

    get_direccion.short_description = "Dirección"

    def get_referencia(self, obj):
        return obj.cliente.referencia

    get_referencia.short_description = "Referencia"

    def get_celular(self, obj):
        return obj.cliente.celular

    get_celular.short_description = "Celular"


admin.site.register(Producto, ProductoAdmin)
admin.site.register(Venta, VentaAdmin)
