from django import forms
from .models import Produto

class AdicionarProdutoForm(forms.Form):
    produto = forms.ModelChoiceField(queryset=Produto.objects.all())