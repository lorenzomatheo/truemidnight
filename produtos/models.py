from django.db import models
from django.contrib.auth.models import User

class Produto(models.Model):
    nome = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    imagem = models.ImageField(upload_to='produtos/', blank=True, null=True)  # Imagem do produto

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'produtos_produto'

class Carrinho(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='carrinhos_produtos')  # related_name adicionado
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'produtos_carrinho'

    def total(self):
        return sum(item.produto.preco * item.quantidade for item in self.itens.all())

class ItemCarrinho(models.Model):
    carrinho = models.ForeignKey(Carrinho, related_name='itens', on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name='itens_produto')  # related_name adicionado
    quantidade = models.PositiveIntegerField(default=1)

    class Meta:
        db_table = 'produtos_itemcarrinho'

    @property
    def preco_total(self):
        return self.produto.preco * self.quantidade
