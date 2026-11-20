from django.db import models

class Producto(models.Model):
    productoID = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=18, decimal_places=2)
    fechaMod = models.DateTimeField(auto_now=True)
    activo = models.BooleanField(default=True)

    class Meta:
        db_table = 'producto'

    def __str__(self):
        return self.nombre


class Pieza(models.Model):
    piezaID = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=300, blank=True, null=True)
    material = models.CharField(max_length=100)
    esOriginal = models.BooleanField(default=True)
    fechaMod = models.DateTimeField(auto_now=True)
    activo = models.BooleanField(default=True)

    class Meta:
        db_table = 'pieza'

    def __str__(self):
        return f"{self.nombre} ({self.material})"


class AsignacionPieza(models.Model):
    asignacionPiezaID = models.AutoField(primary_key=True)
    cantidad = models.IntegerField()
    fechaMod = models.DateTimeField(auto_now=True)
    activo = models.BooleanField(default=True)
    
    # Llaves foráneas (FK)
    piezaID = models.ForeignKey(
        Pieza, 
        on_delete=models.CASCADE, 
        db_column='piezaID',
        related_name='asignaciones'
    )
    productoID = models.ForeignKey(
        Producto, 
        on_delete=models.CASCADE, 
        db_column='productoID',
        related_name='piezas_asignadas'
    )

    class Meta:
        db_table = 'asiganacionPieza'  # Respeta el nombre exacto de tu tabla

    def __str__(self):
        return f"{self.productoID.nombre} -> {self.cantidad}x {self.piezaID.nombre}"