from django.db import models

# Create your models here.

class Materia(models.Model):
    nombre = models.CharField(max_length=30)
    comision = models.IntegerField()

class Alumno(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    carrera = models.CharField(max_length=50)
    

class Profesor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
