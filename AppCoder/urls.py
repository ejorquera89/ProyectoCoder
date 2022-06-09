from django.urls import path
from AppCoder.views import curso, profesores

urlpatterns = [
    path('curso/', curso),  
    path('profesores/', profesores),
]
