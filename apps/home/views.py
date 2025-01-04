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

# Modelos DDSI
from .models import Ingreso  
from .models import Gasto 
from .forms import IngresoForm, GastoForm, ProductoForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

#producto
from .models import Producto

def contabilidad_view(request):
    # Calcular la suma de los ingresos
    total_ingresos = Ingreso.objects.all().aggregate(total=Sum('monto_ingreso'))['total'] or 0

    # Calcular la suma de los gastos
    total_gastos = Gasto.objects.all().aggregate(total=Sum('monto_gasto'))['total'] or 0

    # Calcular el balance neto
    balance_neto = total_ingresos - total_gastos

    # Pasar todo al contexto
    return render(request, 'home/contabilidad.html', {
        'total_ingresos': total_ingresos,
        'total_gastos': total_gastos,
        'balance_neto': balance_neto,
    })
    
@login_required(login_url="/login/")
def ingresos_view(request):
    # BUSCAR INGRESOS
    search_query = request.GET.get('search', '')
    if search_query:
        ingresos = Ingreso.objects.filter(id_ingreso__icontains=search_query)
    else:
        ingresos = Ingreso.objects.all()

    context = {
        'ingresos': ingresos,
    }

    # Manejo de formularios para añadir ingresos y gastos
    if request.method == 'POST':
        if 'add_ingreso' in request.POST:  # Si se pulsa el botón de Ingreso
            ingreso_form = IngresoForm(request.POST)
            if ingreso_form.is_valid():
                ingreso_form.save()
                return redirect('ingresos')  # Redirige a la misma página
        elif 'edit_ingreso' in request.POST:  # Si se pulsa el botón de Editar
            # Obtener el id del ingreso desde el formulario POST
            ingreso_id = request.POST.get('ingreso_id')  # El ID viene con el formulario
            ingreso = get_object_or_404(Ingreso, id_ingreso=ingreso_id)
            ingreso_form = IngresoForm(request.POST, instance=ingreso)
            if ingreso_form.is_valid():
                ingreso_form.save()
                return redirect('ingresos')  # Redirige a la misma página
    else:
        ingreso_form = IngresoForm()

    # Si estamos editando un ingreso, obtenemos ese ingreso
    ingreso_id = request.GET.get('edit', None)
    if ingreso_id:
        ingreso = get_object_or_404(Ingreso, id_ingreso=ingreso_id)
        ingreso_form = IngresoForm(instance=ingreso)

    context['ingreso_form'] = ingreso_form

    html_template = loader.get_template('home/ingresos.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def gastos_view(request):
    # BUSCAR GASTOS
    search_query = request.GET.get('search', '')
    if search_query:
        gastos = Gasto.objects.filter(id_gasto__icontains=search_query)
    else:
        gastos = Gasto.objects.all()

    context = {
        'gastos': gastos,
    }

    # Manejo de formularios para añadir gastos y gastos
    if request.method == 'POST':
        if 'add_gasto' in request.POST:  # Si se pulsa el botón de Gasto
            gasto_form = GastoForm(request.POST)
            if gasto_form.is_valid():
                gasto_form.save()
                return redirect('gastos')  # Redirige a la misma página
        elif 'edit_gasto' in request.POST:  # Si se pulsa el botón de Editar
            # Obtener el id del gasto desde el formulario POST
            gasto_id = request.POST.get('gasto_id')  # El ID viene con el formulario
            gasto = get_object_or_404(Gasto, id_gasto=gasto_id)
            gasto_form = GastoForm(request.POST, instance=gasto)
            if gasto_form.is_valid():
                gasto_form.save()
                return redirect('gastos')  # Redirige a la misma página
    else:
        gasto_form = GastoForm()

    # Si estamos editando un gasto, obtenemos ese gasto
    gasto_id = request.GET.get('edit', None)
    if gasto_id:
        gasto = get_object_or_404(Gasto, id_gasto=gasto_id)
        gasto_form = GastoForm(instance=gasto)

    context['gasto_form'] = gasto_form

    html_template = loader.get_template('home/gastos.html')
    return HttpResponse(html_template.render(context, request))



@login_required(login_url="/login/")
def eliminar_ingreso(request, ingreso_id):
    # Asegurarse de que la solicitud sea POST
    if request.method == 'POST':
        ingreso = get_object_or_404(Ingreso, id_ingreso=ingreso_id)
        ingreso.delete()  # Elimina el ingreso de la base de datos

    return redirect('contabilidad')  # Redirige a la vista de contabilidad

@login_required(login_url="/login/")
def eliminar_gasto(request, gasto_id):
    # Asegurarse de que la solicitud sea POST
    if request.method == 'POST':
        gasto = get_object_or_404(Gasto, id_gasto=gasto_id)
        gasto.delete()  # Elimina el ingreso de la base de datos

    return redirect('contabilidad')  # Redirige a la vista de contabilidad


#productos
#editado para aniadir el restock
@login_required(login_url="/login/")
def productos_view(request):
    # BUSCAR PRODUCTOS
    search_query = request.GET.get('search', '')
    if search_query:
        productos = Producto.objects.filter(ID_producto__icontains=search_query)
    else:
        productos = Producto.objects.all()

    # Productos con cantidad = 0 para el aviso de restock
    productos_sin_stock = Producto.objects.filter(cantidad=0)

    context = {
        'productos': productos,
        'productos_sin_stock': productos_sin_stock,  # Añadido al contexto
    }

    # Manejo de formularios para añadir y editar productos
    if request.method == 'POST':
        if 'add_producto' in request.POST:  # Si se pulsa el botón de Añadir Producto
            producto_form = ProductoForm(request.POST)
            if producto_form.is_valid():
                producto_form.save()
                return redirect('productos')  # Redirige a la misma página
        elif 'edit_producto' in request.POST:  # Si se pulsa el botón de Editar Producto
            # Obtener el id del producto desde el formulario POST
            producto_id = request.POST.get('producto_id')  # El ID viene con el formulario
            producto = get_object_or_404(Producto, ID_producto=producto_id)
            producto_form = ProductoForm(request.POST, instance=producto)
            if producto_form.is_valid():
                producto_form.save()
                return redirect('productos')  # Redirige a la misma página
    else:
        producto_form = ProductoForm()

    # Si estamos editando un producto, obtenemos ese producto
    producto_id = request.GET.get('edit', None)
    if producto_id:
        producto = get_object_or_404(Producto, ID_producto=producto_id)
        producto_form = ProductoForm(instance=producto)

    context['producto_form'] = producto_form

    html_template = loader.get_template('home/productos.html')
    return HttpResponse(html_template.render(context, request))

#eliminar productos
@login_required(login_url="/login/")
def eliminar_producto(request, producto_id):
    # Asegurarse de que la solicitud sea POST
    if request.method == 'POST':
        producto = get_object_or_404(Producto, ID_producto=producto_id)  # Buscar el producto por su ID
        producto.delete()  # Elimina el producto de la base de datos

    return redirect('productos')  # Redirige a la vista de productos


#otros

@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
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
    
    

#crear una vista que sea una clase con sus funciones