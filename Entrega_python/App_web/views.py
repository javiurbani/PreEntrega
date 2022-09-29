from django.shortcuts import *

from App_web.models import *
from django.db.models import *
from .forms import *
# Create your views here.



def profesorFormulario(request):
    
  if request.method == 'POST':
      
    FormularioProfesores = ProfesorForm(request.POST)
    
    print(FormularioProfesores)
    
    if FormularioProfesores.is_valid():
            
            info = FormularioProfesores.cleaned_data

            profesor = Profesor(nombre = info['nombre'],apellido = info['apellido'])

            profesor.save()
            
            return redirect("inicio")
    else:
            return render(request,"App_web/profesores.html",{'FormularioProfesores': FormularioProfesores})
  else:
    FormularioProfesores = ProfesorForm()

    return render(request,"App_web/profesores.html",{'FormularioProfesores': FormularioProfesores})





def alumnoFormulario(request):
    
  if request.method == 'POST':
      
    FormularioAlumno = AlumnoForm(request.POST)
    
    print(FormularioAlumno)
    
    if FormularioAlumno.is_valid:
        
        info = FormularioAlumno.cleaned_data

        alumno = Alumno(nombre = info['nombre'],apellido = info['apellido'],carrera = info['carrera'])

        alumno.save()  

        return redirect("inicio")
    else: 
      return render(request,"App_web/alumnos.html",{'FormularioAlumno': FormularioAlumno})
  else:
      
    FormularioAlumno = AlumnoForm()

  return render(request,"App_web/alumnos.html",{'FormularioAlumno': FormularioAlumno})





def materiaFormulario(request):
    
  if request.method == 'POST':
      
    formularioMaterias = MateriaForm(request.POST)
    
    
    if formularioMaterias.is_valid():
        
        info = formularioMaterias.cleaned_data

        materia = Materia(nombre = info["nombre"],comision = info["comision"])

        materia.save()
        
        return redirect("inicio")
    else:
            return render(request,"App_web/materias.html",{"formularioMaterias":formularioMaterias})
  else:
      
    formularioMaterias = MateriaForm()

  return render(request,"App_web/materias.html",{'formularioMaterias': formularioMaterias})


    
def inicio (request):
  materias = Materia.objects.all()

  profesores= Profesor.objects.all()

  alumnos= Alumno.objects.all()
  if request.method == "POST":

        materia = request.POST["materias"]

        materiasBusqueda = Materia.objects.filter( Q(nombre__icontains=materia) | Q(comision__icontains=materia) ).values()
        
        return render(request,"App_web/index.html",{'materias':materias,'profesores':profesores,'alumnos':alumnos,'materiasBusqueda':materiasBusqueda})

  else: # get y otros

      
      return render(request,"App_web/index.html",{'materias':materias,'profesores':profesores,'alumnos':alumnos})

