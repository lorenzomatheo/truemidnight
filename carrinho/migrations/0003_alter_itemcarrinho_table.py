# Generated by Django 5.1.2 on 2024-11-30 18:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carrinho', '0002_alter_itemcarrinho_table'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='itemcarrinho',
            table='carrinho_itemcarrinho',
        ),
    ]