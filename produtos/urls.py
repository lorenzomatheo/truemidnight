# produtos/urls.py
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.produtos_view, name='produtos'),
    path('adicionar/', views.adicionar_produto_view, name='adicionar_produto'),
    path('adicionar/<int:produto_id>/', views.adicionar_ao_carrinho, name='adicionar_ao_carrinho'),
    path('cart/', views.visualizar_carrinho, name='cart'),
    path('cart/atualizar/<int:item_id>/', views.atualizar_quantidade, name='atualizar_quantidade'),
    path('conta/', include('conta.urls')),
]

if settings.DEBUG:  # Apenas durante o desenvolvimento
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)