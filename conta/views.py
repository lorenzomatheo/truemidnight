from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages

@login_required
def conta_view(request):
    return render(request, 'conta/conta.html')

@login_required
def alterar_email(request):
    if request.method == 'POST':
        novo_email = request.POST.get('email')
        if novo_email:
            request.user.email = novo_email
            request.user.save()
            messages.success(request, 'Email atualizado com sucesso!')
            return redirect('conta')
    return render(request, 'conta/alterar_email.html')

@login_required
def alterar_senha(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Mantém o usuário logado após a troca da senha
            messages.success(request, 'Senha atualizada com sucesso!')
            return redirect('conta')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'conta/alterar_senha.html', {'form': form})
