from django.shortcuts import render,redirect,get_object_or_404
from django.views.decorators.http import require_POST

# Create your views here.
from .models import Usuario

from .forms import UsuarioForm


#Cadastrar os usuarios
def handler405(request,exception):
    return render(request,'usuario/405.html',status=405)

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
@require_POST
def deletar_usuario(request,id_usuario):
    usuario = get_object_or_404(Usuario,id=id_usuario)
    usuario.delete()
    return redirect('listar_usuarios')

def editar_usuario(request,id_usuario):
    usuario=get_object_or_404(Usuario ,pk=id_usuario)
    if request.method=="POST":# tem mesmo de ser com letra maiúscula

        form1=UsuarioForm(request.POST ,instance=usuario)
        if form1.is_valid():
            form1.save()
            return redirect('listar_usuarios')
    else:
        form=UsuarioForm(instance=usuario)
    return render(request, 'usuario/editar.html', {'form1': form, 'usuario': usuario})


    
"""Actualizar usuarios 
        A página de editar tem dois métodos o get e o Post : Ao clicar em editar segundo a viws 
        def editar_usuario(request,id_usuario):
        #Intanciar o objecto tirado do Usuario que tem dados la gravados 
        #Mas com um objecto específico que a url manda atraves do id da url ele vai 
        #mostrar a tal bojecto ,porque nao queremos mostrar todos 
        # Agora assim eu ja posso editar .
        usuario_id = get_object_or_404(Usuario,id=id_usuario)
        # Ele guarda esta instancia e nao faz nada entao testa pela primeiro click se 
        if request.method == 'POST':
            # 2. Criar o formulário com os dados POST e a instância do usuário
            # O parâmetro 'instance=usuario' é crucial para que o formulário saiba qual objeto atualizar
            form = UsuarioForm(request.POST, instance=usuario)
            #este form aqui chama o forUser com estes campos 
               class UsuarioForm(forms.ModelForm):
                class Meta:
                model = Usuario
                fields = ['nome', 'email', 'telefone']
            #so que ele nao cria vazio ele vem com os dados do post ja colocados no get para aquele id 
            #tipos de dados de acordo ao request.Pos dados que eu preeenchi no formulario 
            #{'nome': 'Celsia', 'email': 'celsia@gmail.com', 'idade': '27'}
            # instance=usuario diz ao Django:
     #“depois de mostrar um formulario preenchido com os dados 
    #nstance=usuario diz instancia so este obejecto com o id acima para ser edita .
    #Sem isso ele salvaria de novo
            # Agora se estes dados sao validos ele salva o que eu escrevi
            if form.is_valid():
                # 3. Salvar as alterações na instância existente
                form.save()
                # 4. Redirecionar para a lista de usuários
                return redirect('listar_usuarios')
            #Condicao em primeira instacia pois o método 
            #post ainda nao tem dados entao nao renderiza é considerado o metodo como sendo falso 
            #passa para o else o else é executado
            else:
            # 5. Criar o formulário pré-preenchido com os dados do usuário (GET)
                form = UsuarioForm(instance=usuario)
            #Este aqui apenas pega no form e inicia a instancia do modelo com
            #valores vazios para preencher e renderiza a pagina 
            #esta dizendo pega o usermodel e seu campos nome email e telefone e os mostre aqui
            # entao vai pegar o form vai por na pagina com aquele caracter de procura 
            #apenas para aquele usuario específico com os dados prenchidos nos campos graças ao isntance=usuario 
        # 6. Renderizar o template de edição
        return render(request, 'usuario/editar.html', {'form1': form, 'usuario': usuario_id})
    """

