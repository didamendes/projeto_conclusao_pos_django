from django.urls import path
from . import views

urlpatterns = [
    path('', views.AutorMenuView.as_view(), name='autor_menu'),
    path('autor_create', views.AutorCreateView.as_view(), name='autor_create'),

    path('autor_update/<int:pk>', views.AutorUpdateView.as_view(), name='autor_update'),

    path('autor_delete/<int:pk>', views.AutorDeleteView.as_view(), name='autor_delete'),

    path('cadastro', views.CadastroUsuarioView.as_view(), name='cadastro')
]