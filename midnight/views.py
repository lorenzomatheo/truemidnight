from django import forms
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
from django.db import IntegrityError
from produtos.models import Produto

import re  # Para expressões regulares

# Formulário de cadastro
class CadastroForm(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'senha']  # Use 'senha' aqui, em vez de 'password'
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Um usuário com este e-mail já existe.')
        return email

    def clean_username(self):
        username = self.cleaned_data['username']

        # Permitir espaços e verificar se o username não é vazio
        if not username:
            raise forms.ValidationError('Este campo não pode ficar vazio.')

        # Remover restrições de caracteres
        if not re.match(r'^[\w.@+_-]+$', username):
            raise forms.ValidationError('Informe um nome de usuário válido. Este valor pode conter letras, números e os seguintes caracteres @/./+/-/_.')
        
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Usuário já cadastrado.')  # Corrigido para "Usuário"

        return username

def cadastro_view(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['senha'])  # Corrigido

            try:
                user.save()
                messages.success(request, 'Cadastro realizado com sucesso. Faça o login.')
                return redirect('home')
            except IntegrityError:
                messages.error(request, 'Este e-mail já está cadastrado.')

    else:
        form = CadastroForm()

    return render(request, 'cadastro.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        
        # Verifica se os campos estão vazios
        if not email or not senha:
            messages.error(request, 'Por favor, preencha todos os campos.')
            return render(request, 'login.html')  # Retorna o template com a mensagem de erro
            
        # Tenta encontrar o usuário pelo e-mail
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            user = None

        # Autentica o usuário
        if user is not None and user.check_password(senha):  # Usando check_password para verificar a senha
            login(request, user)
            return redirect('index')  # Altere para a sua página inicial
        else:
            messages.error(request, 'E-mail ou senha incorretos.')
    
    return render(request, 'login.html')  

def index_view(request):
    return render(request, 'index.html')

def cart_view(request):
    return render(request, 'cart.html')

def conta_view(request):
    return render(request, 'conta.html')  # Certifique-se de ter o template 'conta.html'

def produtos_view(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos/produtos.html', {'produtos': produtos})