# carrinho/models.py
from django.db import models
from django.contrib.auth.models import User
from produtos.models import Produto

class Carrinho(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='carrinho')
    criado_em = models.DateTimeField(auto_now_add=True)

    @property
    def total(self):
        return sum(item.produto.preco * item.quantidade for item in self.itens.all())

    def __str__(self):
        return f"Carrinho de {self.usuario.username}"

class ItemCarrinho(models.Model):
    carrinho = models.ForeignKey(Carrinho, related_name='itens', on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)

    def preco_total(self):
        return self.produto.preco * self.quantidade

    def __str__(self):
        return f"{self.quantidade} x {self.produto.nome}"

    class Meta:
        db_table = 'carrinho_itemcarrinho'  # Tabela específica para o app carrinho

