from rest_framework import serializers
from .models import Producto, Pieza, AsignacionPieza

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'


class PiezaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pieza
        fields = '__all__'


class AsignacionPiezaSerializer(serializers.ModelSerializer):
    # Campos extra de solo lectura para facilitar el trabajo en el Frontend
    nombre_producto = serializers.ReadOnlyField(source='productoID.nombre')
    nombre_pieza = serializers.ReadOnlyField(source='piezaID.nombre')

    class Meta:
        model = AsignacionPieza
        fields = [
            'asignacionPiezaID',
            'cantidad',
            'fechaMod',
            'activo',
            'piezaID',
            'nombre_pieza',
            'productoID',
            'nombre_producto',
        ]