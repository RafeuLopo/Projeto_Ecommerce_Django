from django.urls import path, include
from . import views

app_name = 'produto'

urlpatterns = [
    path('', views.ListaProdutos.as_view(), name='lista'),
    path('<slug>', views.DetalheProdutos.as_view(), name='detalhe'),
    path('adicionar/', views.AdicionarAoCarrinho.as_view(), name='adicionar'),
    path('remover/', views.RemoverDoCarrinho.as_view(), name='remover'),
    path('carrinho/', views.Carrinho.as_view(), name='carrinho'),
    path('resumodacompra/', views.ResumoDaCompra.as_view(), name='resumodacompra'),
    path('busca/', views.Busca.as_view(), name='busca'),
]

