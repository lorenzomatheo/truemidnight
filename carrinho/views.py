# carrinho/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Carrinho, ItemCarrinho
from produtos.models import Produto

@login_required
def visualizar_carrinho(request):
    carrinho, _ = Carrinho.objects.get_or_create(usuario=request.user)
    return render(request, 'carrinho/cart.html', {'carrinho': carrinho})

@login_required
def adicionar_ao_carrinho(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    carrinho, _ = Carrinho.objects.get_or_create(usuario=request.user)
    item, item_created = ItemCarrinho.objects.get_or_create(carrinho=carrinho, produto=produto)

    if not item_created:
        item.quantidade += 1
        item.save()

    return redirect('carrinho:visualizar_carrinho')

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

    return redirect('carrinho:visualizar_carrinho')

@login_required
def remover_do_carrinho(request, item_id):
    item = get_object_or_404(ItemCarrinho, id=item_id)
    item.delete()
    return redirect('carrinho:visualizar_carrinho')
