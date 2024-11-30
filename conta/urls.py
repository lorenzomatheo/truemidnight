from django.urls import path
from . import views

urlpatterns = [
    path('', views.conta_view, name='conta'),
    path('alterar_email/', views.alterar_email, name='alterar_email'),
    path('alterar_senha/', views.alterar_senha, name='alterar_senha'),
]
