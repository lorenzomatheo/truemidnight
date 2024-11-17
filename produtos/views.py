# produtos/views.py
from django.shortcuts import render
from produtos.models import Produto

def index_view(request):
    return render(request, 'produtos.html')  # Renderiza a página 'produtos.html'

def cart_view(request):
    return render(request, 'cart.html')

def conta_view(request):
    return render(request, 'conta.html')  # Certifique-se de ter o template 'conta.html'