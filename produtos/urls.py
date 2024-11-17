from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),  # Página inicial
    path('produtos/', include('midnight.urls')),  # Produtos
    path('carrinho/', include('midnight.urls')),  # Carrinho
    path('conta/', include('midnight.urls')),  # Conta
]
