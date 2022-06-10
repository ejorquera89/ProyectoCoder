from django.urls import path
from AppCoder.views import curso, profesores, inicio, cursos, entregables, estudiantes


urlpatterns = [
    path('curso/', curso),  
    path('profesores/', profesores, name = 'Profesores'),
    path('cursos/', cursos, name = 'Cursos'),
    path('entregables/', entregables, name = 'Entregables'),
    path('estudiantes/', estudiantes, name = 'Estudiantes'),
    path('', inicio, name = 'Inicio'),
]
