from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect


def cadastro(requests):
    if requests.user.is_authenticated:
        return redirect('/divulgar/novo_pet')

    if requests.method == "GET":
        return render(requests, 'cadastro.html')
    else:
        nome = requests.POST.get('nome')
        email = requests.POST.get('email')
        senha = requests.POST.get('senha')
        confirmar_senha = requests.POST.get('confirmar_senha')

        if len(nome.strip()) == 0 or len(email.strip()) == 0 or len(senha.strip()) == 0 or len(confirmar_senha.strip()) == 0:
            messages.add_message(requests, constants.ERROR, 'Preencha todos os campos')

            return render(requests, 'cadastro.html')
        
        if senha != confirmar_senha:
            messages.add_message(requests, constants.ERROR, 'Digite duas senhas iguais')
            return render(requests, 'cadastro.html')
        try:
            user = User.objects.create_user(username = nome, email = email,password= senha)
            messages.add_message(requests, constants.SUCCESS, 'Usuário criado com suceso')
            return render(requests, 'cadastro.html')
        except:
            messages.add_message(requests, constants.ERROR, 'Erro interno no sistema')
            return render(requests, 'cadastro.html')

def logar(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == "POST":
        nome = request.POST.get("nome")
        senha = request.POST.get("senha")
        user = authenticate(username = nome, password = senha)
    
    if user is not None:
        login(request, user)
        return redirect('/divulgar/novo_pet')
    else:
        messages.add_message(request, constants.ERROR, 'Usúario ou senha incorretos!')
        return render(request, 'login.html')

def sair(request):
    logout (request)
    return redirect('/auth/login')