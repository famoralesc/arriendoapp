from arriendo.entities import models
from django.contrib import admin

# Register your models here.
@admin.register(models.Cliente)
class ClienteAdmin(admin.ModelAdmin):
    pass

@admin.register(models.TipoOperacion)
class TipoOperacionAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Operacion)
class OperacionAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Comprobante)
class ComprobanteAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Propiedad)
class PropiedadAdmin(admin.ModelAdmin):
    pass

