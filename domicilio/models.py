from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Cargo(models.Model):
    id_cargo=models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.tipo

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
#----------------------------------------------------
class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nombre_cliente = models.CharField(max_length=100)
    apellido_cliente = models.CharField(max_length=100)
    telefono = models.PositiveIntegerField(validators=[RegexValidator(r'^\d{8,8}$')])
    direccion = models.TextField()

    def __str__(self):
        return  self.nombre_cliente +" "+ self.apellido_cliente

class Orden(models.Model):
    id_orden = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    hora_orden = models.TimeField()
    detalle = models.CharField(max_length=100)
    direccion = models.TextField()

    def __str__(self):
        return "Numero de Orden: "+str(self.id_orden)

