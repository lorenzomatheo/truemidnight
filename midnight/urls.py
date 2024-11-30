# midnight/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cadastro/', views.cadastro_view, name='cadastro_view'),
    path('login/', views.login_view, name='login_view'),
    path('', views.login_view, name='home'),  # Página inicial
    path('index/', views.index_view, name='index'),
    path('produtos/', include('produtos.urls')),
    path('carrinho/', include('carrinho.urls')),
    path('conta/', include('conta.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
