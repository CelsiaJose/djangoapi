from rest_framework import viewsets
from .models import Usuario
from .serializers import UsuarioSerializer

class UsuarioViewset(viewsets.ModelViewSet):

    #O viewset ja faz as operacoes listar,criar,buscadetalhada,elimniar e actualizar
    #variável que busca os dados no modelo

    queryset=Usuario.objects.all()
    # Define o Serializer a ser usado para converter dados
    serializer_class = UsuarioSerializer
# passo a seguir definir rotas
