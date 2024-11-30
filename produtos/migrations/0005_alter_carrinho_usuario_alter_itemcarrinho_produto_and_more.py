# Generated by Django 5.1.2 on 2024-11-26 16:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0004_remove_itemcarrinho_preco_alter_carrinho_table_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrinho',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='carrinhos_produtos', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='itemcarrinho',
            name='produto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itens_produto', to='produtos.produto'),
        ),
        migrations.AlterModelTable(
            name='carrinho',
            table='produtos_carrinho',
        ),
    ]
