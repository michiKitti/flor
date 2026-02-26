from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('lista/', views.lista_flores, name='lista_flores'),
    path('crear/', views.crear_flor, name='crear_flor'),
    path('eliminar/<int:id>/', views.eliminar_flor, name='eliminar_flor'),
]