from django.db import models



class Producto(models.Model):
    nombre_Producto = models.CharField(max_length=50)
    unidades = models.CharField(max_length=50)
    precio = models.CharField(max_length=50)
    
    def __str__(self) :
        return f"{self.id} - {self.nombre_producto}"


class Compra(models.Model):
    fecha_compra = models.CharField(max_length=50)
    proveedor = models.CharField(max_length=50)
    importe_compra = models.CharField(max_length=50)
    
    def __str__(self) :
        return f"{self.id} - {self.proveedor}"

class Proveedor(models.Model):
    nombre = models.CharField(max_length=50)
    domicilio = models.CharField(max_length=50)
    contacto = models.CharField(max_length=50)
    
    def __str__(self) :
        return f"{self.id} - {self.nombre}"
    







