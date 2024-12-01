# produtos/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Produto, Carrinho, ItemCarrinho
from .forms import ProdutoForm
from django.contrib.auth.models import User
from django.db import models


def index_view(request):
    return render(request, 'produtos/produtos.html')

@login_required
def produtos_view(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos/produtos.html', {'produtos': produtos})

@login_required
def adicionar_produto_view(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('produtos')
    else:
        form = ProdutoForm()
    return render(request, 'produtos/adicionar_produto.html', {'form': form})

@login_required
def adicionar_ao_carrinho(request, produto_id):
    # Busca o produto pelo ID ou retorna 404
    produto = get_object_or_404(Produto, id=produto_id)

    # Garante que existe um carrinho para o usuário atual
    carrinho, _ = Carrinho.objects.get_or_create(usuario=request.user)

    # Busca ou cria um item do carrinho relacionado ao produto
    item, item_created = ItemCarrinho.objects.get_or_create(carrinho=carrinho, produto=produto)

    # Faltando z

    # Se o item já existir no carrinho, incrementa a quantidade
    if not item_created:
        item.quantidade += 1
        item.save()

    # Redireciona para a página do carrinho
    return redirect('cart')  # Certifique-se de que a URL "cart" está configurada corretamente


@login_required
def atualizar_quantidade(request, item_id):
    item = get_object_or_404(ItemCarrinho, id=item_id)
    
    if request.method == 'POST':
        action = request.POST.get('action')
        
        if action == 'increment':
            item.quantidade += 1
        elif action == 'decrement' and item.quantidade > 1:
            item.quantidade -= 1

        item.save()

    return redirect('cart')

def conta_view(request):
    return render(request, 'conta.html')

@login_required
def visualizar_carrinho(request):
    carrinho = Carrinho.objects.filter(usuario=request.user).first()
    return render(request, 'carrinho/cart.html', {'carrinho': carrinho})
