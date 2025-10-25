from django.contrib import admin

# Register your models here.
#Adicionados os models no admin

from usuarios.models import Usuario

admin.site.register(Usuario)
