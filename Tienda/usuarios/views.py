from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import *
from .forms import RegisterUserForm


def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('Inicio')
        else:
            messages.success(request, ("Ingrese datos validos"))
            return redirect('login_user')
    
    else:
        return render(request, 'authenticate/login.html')


def registrar_user(request):
        if request.method == "POST":
             form = UserCreationForm(request.POST)
             if form.is_valid():
                  form.save()
                  username = form.cleaned_data['username']
                  password = form.cleaned_data['password1']
                  user = authenticate(username=username, password=password)
                  login(request, user)
                  messages.success(request, ("Registro Completado"))
                  return redirect('Inicio')
        else:
            form = UserCreationForm()

        return render(request, 'authenticate/registrar_usuario.html', {'form':form,})

def logout_user(request):
    logout(request)
    return redirect('Inicio')


# def registrar_user(request):
#         if request.method == "POST":
#              form = RegisterUserForm(request.POST)
#              if form.is_valid():
#                   form.save()
#                   username = form.cleaned_data['username']
#                   password = form.cleaned_data['password1']
#                   user = authenticate(username=username, password=password)
#                   login(request, user)
#                   messages.success(request, ("Registro Completado"))
#                   return redirect('Inicio')
#         else:
#             form = RegisterUserForm()

#         return render(request, 'authenticate/registrar_usuario.html', {'form':form,})