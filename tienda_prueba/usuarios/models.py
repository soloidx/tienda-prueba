from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Usuario(AbstractUser):
    DOCUMENT_TYPES = [("DNI", "DNI"), ("RUC", "RUC")]
    tipo_documento = models.CharField(max_length=10, choices=DOCUMENT_TYPES)
    numero_documento = models.CharField(max_length=10, blank=True)
    direccion = models.TextField(blank=True)
    referencia = models.TextField(blank=True)
    celular = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @staticmethod
    def autocomplete_search_fields():
        return (
            "first_name__icontains",
            "last_name__icontains",
            "numero_documento__iexact",
        )
