from django.urls import path
from . import views

urlpatterns = [
    path('', views.autor_menu.as_view(), name='autor_menu'),
    path('autor_create', views.autor_create.as_view(), name='autor_create'),

    path('autor_update/<int:pk>', views.autor_update.as_view(), name='autor_update'),

    path('autor_delete/<int:pk>', views.autor_delete.as_view(), name='autor_delete')
]