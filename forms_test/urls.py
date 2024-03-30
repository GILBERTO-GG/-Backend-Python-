#from django.contrib import admin
from django.urls import path
from .views import register, registro_exitoso



urlpatterns = [
    #path("admin/", admin.site.urls),
    path('registro/', register, name='registro'),
    path('registro_exitoso/', registro_exitoso, name='registro_exitoso'),
]