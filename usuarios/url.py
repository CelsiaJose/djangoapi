from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views #from usuarios import views
from .views_api import UsuarioViewset #from usuarios import views_api tem apenas uma funcao então importo direito
# Cria um router e regista o nosso ViewSet
#cria um roteamento para a classe criada no viewset
router = DefaultRouter()
#Criar a rota e o endpoint
router.register(r'usuarios', UsuarioViewset)# O prefixo 'usuarios' define o endpoint da API (ex: /api/usuarios/)

urlpatterns = [
    # URLs da API (Geradas automaticamente pelo router)
    # Incluímos o router.urls sob o prefixo 'api/'
    path('api/', include(router.urls)),

        # URLs Tradicionais (HTML) - Mantidas para o seu CRUD original

    path('', views.listar_usuarios, name='listar_usuarios'),
    path('cadastrar/', views.cadastrar_usuario, name='cadastrar_usuario'),
    path('deletar/<int:id_usuario>/', views.deletar_usuario, name='deletar_usuario'),
    path('editar/<int:id_usuario>/',views.editar_usuario,name='editar_usuario'),
]

