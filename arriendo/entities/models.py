from django.db import models

class Cliente(models.Model):
    rut = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return f'{self.nombre} {self.apellido}'
    
    class Meta:
        verbose_name_plural = "Clientes"

class Propiedad(models.Model):
    rol = models.CharField(max_length=50, unique=True)
    dueno = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='propiedades')
    direccion = models.CharField(max_length=200)

    def __str__(self):
        return self.direccion

    class Meta:
        verbose_name_plural = "Propiedades"

class TipoOperacion(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name_plural = "Tipo Operacion"

class Operacion(models.Model):
    tipo = models.ForeignKey(TipoOperacion, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    propiedad = models.ForeignKey(Propiedad, on_delete=models.CASCADE)
    monto_operacion = models.DecimalField(max_digits=10, decimal_places=2)
    comision = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.tipo.nombre} - {self.propiedad.direccion}'

    class Meta:
        verbose_name_plural = "Operaciones"

class Comprobante(models.Model):
    operacion = models.ForeignKey(Operacion, on_delete=models.CASCADE, related_name='comprobantes')
    documento_url = models.URLField()

    def __str__(self):
        return f'Comprobante de {self.operacion}'
    
    class Meta:
        verbose_name_plural = "Comprobantes"