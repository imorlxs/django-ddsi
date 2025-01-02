# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from .forms import LoginForm, SignUpForm
from .forms import EmpleadoForm
from .models import Empleado

def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'

    return render(request, "accounts/login.html", {"form": form, "msg": msg})


def register_user(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg = 'User created - please <a href="/login">login</a>.'
            success = True

            # return redirect("/login/")

        else:
            msg = 'Form is not valid'
    else:
        form = SignUpForm()

    return render(request, "accounts/register.html", {"form": form, "msg": msg, "success": success})


def registrar_empleado(request,action,empleado_id=None):
    if action == 'listar':
        empleados = Empleado.objects.all()
        return render(request,'empleados/empleados.html',{'action':'listar','empleados':empleados})
    elif action == 'registrar':
        if request.method == 'POST':
            form = EmpleadoForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('empleado',action='listar')
        else:
            form = EmpleadoForm()
        return render(request,'empleados/empleados.html',{'action': 'registrar', 'form': form})
    
    elif action == 'modificar':
        empleado = get_object_or_404(Empleado,id=empleado_id)
        if request.method == 'POST':
            form=EmpleadoForm(request.POST, instance=empleado)
            if form.is_valid():
                form.save()
                return redirect('empleado', action='listar')
        else:
            form = EmpleadoForm(instance=empleado)
        return render(request,'empleados/empleados.html',{'action': 'modificar', 'form': form,'empleado': empleado})
    elif action == 'consultar':
        empleado = get_object_or_404(Empleado,id=empleado_id)
        return render(request,'empleados/empleados.html',{'action':'consultar', 'empleado':empleado})
    elif action == 'eliminar':
        empleado = get_object_or_404(Empleado,id=empleado_id)
        empleado.delete()
        return redirect('empleado',action='listar')