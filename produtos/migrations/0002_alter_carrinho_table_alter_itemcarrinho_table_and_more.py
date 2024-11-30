from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0001_initial'),  # Dependência da migração inicial
    ]

    operations = [
        # Alterando o nome da tabela 'produto' (somente se necessário)
        migrations.AlterModelTable(
            name='produto',
            table='produtos_produto',
        ),
        
        # Adicionando o campo 'preco' à tabela 'produtos_itemcarrinho'
        migrations.AddField(
            model_name='itemcarrinho',
            name='preco',
            field=models.DecimalField(max_digits=10, decimal_places=2, null=False),
        ),
        
        # Adicionando a chave estrangeira para 'produtos_carrinho'
        migrations.AddField(
            model_name='itemcarrinho',
            name='carrinho',
            field=models.ForeignKey(to='produtos.Carrinho', on_delete=models.CASCADE),
        ),
        
        # Adicionando a chave estrangeira para 'produtos'
        migrations.AddField(
            model_name='itemcarrinho',
            name='produto',
            field=models.ForeignKey(to='produtos.Produto', on_delete=models.CASCADE),
        ),
    ]
