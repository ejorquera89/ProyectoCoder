from django.contrib import admin
from django.urls import path, include
import AppCoder
from AppCoder.views import curso

urlpatterns = [
    path('admin/', admin.site.urls),
    path('AppCoder/', include('AppCoder.urls')),
]
