from django.shortcuts import render,redirect

# Create your views here.
from .models import Usuario

from .forms import UsuarioForm


#Cadastrar os usuarios

def cadastrar_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_usuarios')
    else:
        form = UsuarioForm()
    return render(request, 'usuario/cadastrar.html', {'form1': form})
#Listar os usuarios

def listar_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request,'usuario/listar.html', {'pessoa': usuarios})
    
#deletar usuarios


#Actualizar usuarios