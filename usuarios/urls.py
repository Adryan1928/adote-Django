from django.urls import path
from . import views

urlpatterns = [
    path('Cadastro/', views.cadastro, name = "Cadastro"),
    path('login/', views.logar, name= "login"),
    path('sair/', views.sair, name = "sair"),
]