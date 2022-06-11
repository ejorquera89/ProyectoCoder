import imp
from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import Curso, Profesor
from django.template import loader
from AppCoder.forms import CursoFormulario
from AppCoder.forms import ProfesorFormulario
# Create your views here.

def curso(self):
    curso = Curso(nombre = "Desarrollo Web", camada = 16740)
    curso.save()
    documento = f"Curso: {curso.nombre} - Camada: {curso.camada}"
    return HttpResponse(documento)

def profesores(request):
    return render(request, 'AppCoder/profesores.html')

def cursos(self):
    documento = f"Página de cursos"
    return HttpResponse(documento)

def estudiantes(self):
    documento = f"Página de estudiantes"
    return HttpResponse(documento)

def entregables(self):
    documento = f"Página de entregables"
    return HttpResponse(documento)  

def inicio(self):
    plantilla = loader.get_template('AppCoder/inicio.html')
    documento = plantilla.render()
    return HttpResponse(documento)

def cursoFormulario(request):
    if request.method == 'POST':
        miFormulario = CursoFormulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
        nombre = informacion ['curso']
        camada = informacion ['camada']
        curso = Curso(nombre = nombre, camada = camada)
        curso.save()
        return render (request, 'AppCoder/inicio.html')
    else:
        miFormulario = CursoFormulario()
    return render (request, 'AppCoder/cursoFormulario.html', {'miFormulario': miFormulario})

def profesorFormulario(request):
    if request.method == 'POST':
        miFormulario = ProfesorFormulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
        nombre = informacion ['nombre']
        apellido = informacion ['apellido']
        email = informacion ['email']
        profesion = informacion ['profesion']
        profesor = Profesor(nombre = nombre, apellido = apellido, email = email, profesion = profesion)
        profesor.save()
        return render (request, 'AppCoder/inicio.html')
    else:
        miFormulario = ProfesorFormulario()
    return render (request, 'AppCoder/profesorFormulario.html', {'miFormulario': miFormulario})

def busquedaCamada(request):
    return render (request, 'AppCoder/busquedaCamada.html')

def buscar(request):
    #respuesta = f"Estoy buscando la comision {request.GET['camada']}"
    #return HttpResponse(respuesta)
    if request.GET['camada']:
        camada = request.GET['camada']
        cursos = Curso.objects.filter(camada = camada)
        return render(request, 'AppCoder/resultadosBusqueda.html', {'cursos': cursos, 'camada': camada})
    else:
        respuesta = "No se ha ingresado ninguna comisión"
    return HttpResponse(respuesta)



