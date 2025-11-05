from rest_framework import viewsets
from .models import Usuario
from .serializers import UsuarioSerializer
#toke para api
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

#@api_view(['GET']) decoate se fosse o api view
#@permission_classes([IsAuthenticated])# terceira linha do viewset como atributo de calsse
class UsuarioViewset(viewsets.ModelViewSet):

    #O viewset ja faz as operacoes listar,criar,buscadetalhada,elimniar e actualizar
    #variável que busca os dados no modelo

    queryset = Usuario.objects.all()
    # Define o Serializer a ser usado para converter dados
    serializer_class = UsuarioSerializer
    # O viewset me permite usar classes e o apiview usa funções e para funçoes usamos o decorate
    # ja em classes os atribustos: quando tem esta classe ele nao vai permitir mostra nada sem a autenticacao  
    permission_classes = [IsAuthenticated]
    viewset=['GET']