"""
URL configuration for cadastro_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
#from usuarios.views import handler405 as handler405_view 


urlpatterns = [

    #INCLUI TODAS AS URL DO APP USUARIOS

    path('', include('usuarios.url')),
    #INCLUI A URL DO DJANGO PARA ADMIN
    path('admin/', admin.site.urls),
    #Estás o url que estão na rota principal vão em seu proprio fixeiro  
]



