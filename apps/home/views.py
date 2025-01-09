# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import loader
from django.urls import reverse
from django.db.models import Sum
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

# Modelos y formularios
from .models import Ingreso, Gasto, Socio, Campana
from .forms import IngresoForm, GastoForm, SocioForm, CampanaForm


def contabilidad_view(request):
    total_ingresos = Ingreso.objects.all().aggregate(total=Sum('monto_ingreso'))['total'] or 0
    total_gastos = Gasto.objects.all().aggregate(total=Sum('monto_gasto'))['total'] or 0
    balance_neto = total_ingresos - total_gastos
    return render(request, 'home/contabilidad.html', {
        'total_ingresos': total_ingresos,
        'total_gastos': total_gastos,
        'balance_neto': balance_neto,
    })


@login_required(login_url="/login/")
def ingresos_view(request):
    search_query = request.GET.get('search', '')
    ingresos = Ingreso.objects.filter(id_ingreso__icontains=search_query) if search_query else Ingreso.objects.all()
    context = {'ingresos': ingresos}
    if request.method == 'POST':
        if 'add_ingreso' in request.POST:
            ingreso_form = IngresoForm(request.POST)
            if ingreso_form.is_valid():
                ingreso_form.save()
                return redirect('ingresos')
        elif 'edit_ingreso' in request.POST:
            ingreso_id = request.POST.get('ingreso_id')
            ingreso = get_object_or_404(Ingreso, id_ingreso=ingreso_id)
            ingreso_form = IngresoForm(request.POST, instance=ingreso)
            if ingreso_form.is_valid():
                ingreso_form.save()
                return redirect('ingresos')
    else:
        ingreso_form = IngresoForm()

    ingreso_id = request.GET.get('edit', None)
    if ingreso_id:
        ingreso = get_object_or_404(Ingreso, id_ingreso=ingreso_id)
        ingreso_form = IngresoForm(instance=ingreso)

    context['ingreso_form'] = ingreso_form
    html_template = loader.get_template('home/ingresos.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def gastos_view(request):
    search_query = request.GET.get('search', '')
    gastos = Gasto.objects.filter(id_gasto__icontains=search_query) if search_query else Gasto.objects.all()
    context = {'gastos': gastos}
    if request.method == 'POST':
        if 'add_gasto' in request.POST:
            gasto_form = GastoForm(request.POST)
            if gasto_form.is_valid():
                gasto_form.save()
                return redirect('gastos')
        elif 'edit_gasto' in request.POST:
            gasto_id = request.POST.get('gasto_id')
            gasto = get_object_or_404(Gasto, id_gasto=gasto_id)
            gasto_form = GastoForm(request.POST, instance=gasto)
            if gasto_form.is_valid():
                gasto_form.save()
                return redirect('gastos')
    else:
        gasto_form = GastoForm()

    gasto_id = request.GET.get('edit', None)
    if gasto_id:
        gasto = get_object_or_404(Gasto, id_gasto=gasto_id)
        gasto_form = GastoForm(instance=gasto)

    context['gasto_form'] = gasto_form
    html_template = loader.get_template('home/gastos.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def eliminar_ingreso(request, ingreso_id):
    if request.method == 'POST':
        ingreso = get_object_or_404(Ingreso, id_ingreso=ingreso_id)
        ingreso.delete()
    return redirect('contabilidad')


@login_required(login_url="/login/")
def eliminar_gasto(request, gasto_id):
    if request.method == 'POST':
        gasto = get_object_or_404(Gasto, id_gasto=gasto_id)
        gasto.delete()
    return redirect('contabilidad')


@login_required(login_url="/login/")
def listar_socios(request):
    search_query = request.GET.get('search', '')
    socios = Socio.objects.filter(nombreSocio__icontains=search_query) if search_query else Socio.objects.all()
    return render(request, 'socios/listar_socios.html', {'socios': socios})


@login_required(login_url="/login/")
def alta_socio(request):
    if request.method == 'POST':
        form = SocioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Socio añadido con éxito.')
            return redirect('listar_socios')
    else:
        form = SocioForm()
    return render(request, 'socios/alta_socio.html', {'form': form})


@login_required(login_url="/login/")
def modificar_socio(request, DNISocio):
    socio = get_object_or_404(Socio, DNISocio=DNISocio)
    if request.method == 'POST':
        form = SocioForm(request.POST, instance=socio)
        if form.is_valid():
            form.save()
            messages.success(request, 'Información del socio actualizada.')
            return redirect('listar_socios')
    else:
        form = SocioForm(instance=socio)
    return render(request, 'socios/modificar_socio.html', {'form': form})


@login_required(login_url="/login/")
def baja_socio(request, DNISocio):
    socio = get_object_or_404(Socio, DNISocio=DNISocio)
    if request.method == 'POST':
        socio.fecha_bajaSocio = request.POST.get('fecha_baja')
        socio.motivo_bajaSocio = request.POST.get('motivo_baja')
        socio.save()
        messages.success(request, 'Socio dado de baja.')
        return redirect('listar_socios')
    return render(request, 'socios/baja_socio.html', {'socio': socio})


@login_required(login_url="/login/")
def detalle_socio(request, DNISocio):
    socio = get_object_or_404(Socio, DNISocio=DNISocio)
    return render(request, 'socios/detalle_socio.html', {'socio': socio})


@login_required(login_url="/login/")
def campanas_view(request):
    search_query = request.GET.get('search', '')
    campanas = Campana.objects.filter(nombre_campana__icontains=search_query) if search_query else Campana.objects.all()
    context = {'campanas': campanas}
    if request.method == 'POST':
        if 'edit_campana' in request.POST:
            campana_id = request.POST.get('campana_id')
            if campana_id:
                campana = get_object_or_404(Campana, id_campana=campana_id)
                campana_form = CampanaForm(request.POST, instance=campana)
                if campana_form.is_valid():
                    campana_form.save()
                    messages.success(request, "¡Campaña editada con éxito!")
                    return redirect('campanas')
                else:
                    messages.error(request, "Errores en el formulario.")
        elif 'add_campana' in request.POST:
            campana_form = CampanaForm(request.POST)
            if campana_form.is_valid():
                campana_form.save()
                messages.success(request, "¡Nueva campaña agregada!")
                return redirect('campanas')
            else:
                messages.error(request, "Errores en el formulario.")
    else:
        campana_form = CampanaForm()

    context['campana_form'] = campana_form
    html_template = loader.get_template('home/campanas.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def eliminar_campana(request, id_campana):
    if request.method == 'POST':
        campana = get_object_or_404(Campana, id_campana=id_campana)
        campana.delete()
    return redirect('campanas')


@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}
    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    try:
        load_template = request.path.split('/')[-1]
        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template
        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))
    except template.TemplateDoesNotExist:
        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))
    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
