from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_flor, name='lista_flores'),
    path('flores/', views.lista_flor, name='lista_flores_alt'),
    path('crear/', views.crear_flor, name='crear_flor'),
    path('editar/<int:id>/', views.editar_flor, name='editar_flor'),
    path('eliminar/<int:id>/', views.eliminar_flor, name='eliminar_flor'),
]