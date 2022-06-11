from django.urls import path
from AppCoder.views import busquedaCamada, curso, profesores, inicio, cursos, entregables, estudiantes, cursoFormulario,profesorFormulario, busquedaCamada, buscar


urlpatterns = [
    path('curso/', curso),  
    path('profesores/', profesores, name = 'Profesores'),
    path('cursos/', cursos, name = 'Cursos'),
    path('entregables/', entregables, name = 'Entregables'),
    path('estudiantes/', estudiantes, name = 'Estudiantes'),
    path('', inicio, name = 'Inicio'),
    path('cursoFormulario/', cursoFormulario, name = 'cursoFormulario'),
    path('profesorFormulario/', profesorFormulario, name = 'profesorFormulario'),
    path('busquedaCamada/', busquedaCamada, name = 'busquedaCamada'),
    path('buscar/', buscar, name = 'buscar'),
]
