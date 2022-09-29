from django import forms


class ProfesorForm(forms.Form):
 nombre = forms.CharField(max_length=30,label="nombre")
 apellido = forms.CharField(max_length=30,label="apellido")

class AlumnoForm(forms.Form):
  nombre = forms.CharField(max_length=30,label="nombre")
  apellido = forms.CharField(max_length=30,label="apellido")
  carrera = forms.CharField(max_length=30,label="carrera")
 

class MateriaForm(forms.Form):
    nombre = forms.CharField(max_length=30,label="Curso")
    comision = forms.IntegerField(min_value=0,label="Comision")