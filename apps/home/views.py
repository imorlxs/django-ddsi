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

# Modelos DDSI
from .models import Ingreso, Gasto, Campana, Empleado, Producto, Socio, Ordena, Compra
from .forms import IngresoForm, GastoForm, CampanaForm, EmpleadoForm, ProductoForm, SocioForm, OrdenaForm, CompraForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages


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
        'segment': 'ingresos',
    }

    # Manejo de formularios para anadir ingresos y gastos
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
        'segment': 'gastos',
    }

    # Manejo de formularios para anadir gastos y gastos
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

    return redirect('ingresos')  

@login_required(login_url="/login/")
def eliminar_gasto(request, gasto_id):
    # Asegurarse de que la solicitud sea POST
    if request.method == 'POST':
        gasto = get_object_or_404(Gasto, id_gasto=gasto_id)
        gasto.delete()  # Elimina el ingreso de la base de datos

    return redirect('gastos')  

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
    
    
@login_required(login_url="/login/")
def campanas_view(request):
    # Search query
    search_query = request.GET.get('search', '')
    if search_query:
        campanas = Campana.objects.filter(nombre_campana__icontains=search_query)
    else:
        campanas = Campana.objects.all()

    context = {
        'campanas': campanas,
        'segment': 'campanas',
    }

    # Modules Management
    campana_form = CampanaForm()  # Always initialize the form at the beginning

    if request.method == 'POST':
        # Verify that the campaign edit has been clicked
        if 'edit_campana' in request.POST:
            campana_id = request.POST.get('campana_id')
            if campana_id:
                # Get the corresponding campaign
                campana = get_object_or_404(Campana, id_campana=campana_id)
                campana_form = CampanaForm(request.POST, instance=campana)

                # If the form is valid, we save the data
                if campana_form.is_valid():
                    campana_form.save()
                    messages.success(request, "¡Campaña editada con éxito!")
                    return redirect('campanas')  # Redirects to the view of the campaign
                else:
                    # Add an error message if the form is invalid
                    messages.error(request, "Hay algunos errores en el formulario.")
            else:
                messages.error(request, "No se encontró el ID de campaña.")
        
        # Verify that adding a new campaign has been clicked
        elif 'add_campana' in request.POST:
            campana_form = CampanaForm(request.POST)  # Create a new form with the submitted data

            # If the form is valid, we save the data
            if campana_form.is_valid():
                campana_form.save()
                messages.success(request, "¡Nueva campaña agregada exitosamente!")
                return redirect('campanas')  # Redirects to the view of the campaign
            else:
                # Add an error message if the form is invalid
                messages.error(request, "Hay algunos errores en el formulario.")

    context['campana_form'] = campana_form

    # Template path
    html_template = loader.get_template('home/campanas.html')  
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def eliminar_campana(request, id_campana):
    # Make sure the request is POST
    if request.method == 'POST':
        campana = get_object_or_404(Campana, id_campana=id_campana)
        campana.delete()  # Delete the campaign from the database

    return redirect('campanas')  # redirects to the view of the campaign 


@login_required(login_url="/login/")
def empleados_view(request):
        # Search query
        search_query = request.GET.get('search', '')
        if search_query:
            empleados = Empleado.objects.filter(DNIEmpleado__icontains=search_query)
        else:
            empleados = Empleado.objects.all()
    
        context = {
            'empleados': empleados,
            'segment': 'empleados',
        }
    
        # Employee form management
        empleado_form = EmpleadoForm()  # Always initialize the form at the beginning
    
        if request.method == 'POST':
            # Verify that the employee edit has been clicked
            if 'edit_empleado' in request.POST:
                empleado_id = request.POST.get('DNIEmpleado')
                if empleado_id:
                    # Get the corresponding employee
                    empleado = get_object_or_404(Empleado, DNIEmpleado=empleado_id)
                    empleado_form = EmpleadoForm(request.POST, instance=empleado)
    
                    # If the form is valid, we save the data
                    if empleado_form.is_valid():
                        empleado_form.save()
                        messages.success(request, "¡Empleado editado con éxito!")
                        return redirect('empleados')  # Redirects to the view of the employees
                    else:
                        # Add an error message if the form is invalid
                        messages.error(request, "Hay algunos errores en el formulario.")
                else:
                    messages.error(request, "No se encontró el ID del empleado.")
            
            # Verify that adding a new employee has been clicked
            elif 'add_empleado' in request.POST:
                empleado_form = EmpleadoForm(request.POST)  # Create a new form with the submitted data
    
                # If the form is valid, we save the data
                if empleado_form.is_valid():
                    empleado_form.save()
                    messages.success(request, "¡Nuevo empleado agregado exitosamente!")
                    return redirect('empleados')  # Redirects to the view of the employees
                else:
                    # Add an error message if the form is invalid
                    messages.error(request, "Hay algunos errores en el formulario.")
    
        context['empleado_form'] = empleado_form
    
        # Template path
        html_template = loader.get_template('home/empleados.html')  
        return HttpResponse(html_template.render(context, request))
    
    
@login_required(login_url="/login/")
def eliminar_empleado(request, DNIEmpleado):
    # Make sure the request is POST
    if request.method == 'POST':
        empleado = get_object_or_404(Empleado, DNIEmpleado=DNIEmpleado)
        empleado.delete()  # Delete the employee from the database
    
    return redirect('empleados')  # Redirects to the view of the employees


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
        'segment': 'productos',
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
            producto_id = request.POST.get('ID_producto')  # El ID viene con el formulario
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
def eliminar_producto(request, ID_producto):
    # Asegurarse de que la solicitud sea POST
    if request.method == 'POST':
        producto = get_object_or_404(Producto, ID_producto=ID_producto)  # Buscar el producto por su ID
        producto.delete()  # Elimina el producto de la base de datos

    return redirect('productos')  # Redirige a la vista de productos

@login_required(login_url="/login/")
def socios_view(request):
        # Search query
        search_query = request.GET.get('search', '')
        if search_query:
            socios = Socio.objects.filter(DNISocio__icontains=search_query)
        else:
            socios = Socio.objects.all()
    
        context = {
            'socios': socios,
            'segment': 'socios',
        }
    
        # Employee form management
        socio_form = SocioForm()  # Always initialize the form at the beginning
    
        if request.method == 'POST':
            # Verify that the employee edit has been clicked
            if 'edit_socio' in request.POST:
                socio_id = request.POST.get('DNISocio')
                if socio_id:
                    # Get the corresponding employee
                    socio = get_object_or_404(Socio, DNISocio=socio_id)
                    socio_form = SocioForm(request.POST, instance=socio)
    
                    # If the form is valid, we save the data
                    if socio_form.is_valid():
                        socio_form.save()
                        messages.success(request, "¡Socio editado con éxito!")
                        return redirect('socios')  # Redirects to the view of the employees
                    else:
                        # Add an error message if the form is invalid
                        messages.error(request, "Hay algunos errores en el formulario.")
                else:
                    messages.error(request, "No se encontró el ID del socio.")
            
            # Verify that adding a new employee has been clicked
            elif 'add_socio' in request.POST:
                socio_form = SocioForm(request.POST)  # Create a new form with the submitted data
    
                # If the form is valid, we save the data
                if socio_form.is_valid():
                    socio_form.save()
                    messages.success(request, "¡Nuevo socio agregado exitosamente!")
                    return redirect('socios')  # Redirects to the view of the employees
                else:
                    # Add an error message if the form is invalid
                    messages.error(request, "Hay algunos errores en el formulario.")
    
        context['socio_form'] = socio_form
    
        # Template path
        html_template = loader.get_template('home/socios.html')  
        return HttpResponse(html_template.render(context, request))
    
    
@login_required(login_url="/login/")
def eliminar_socio(request, DNISocio):
    # Make sure the request is POST
    if request.method == 'POST':
        socio = get_object_or_404(Socio, DNISocio=DNISocio)
        socio.delete()  # Delete the employee from the database
    
    return redirect('socios')  # Redirects to the view of the employees


@login_required(login_url="/login/")
def ordenar_view(request):
    # BUSCAR ORDENAS
    search_query = request.GET.get('search', '')
    if search_query:
        ordenas = Ordena.objects.filter(id_ordena__icontains=search_query)
    else:
        ordenas = Ordena.objects.all()
    context = {
        'ordenas': ordenas,
        'segment': 'ordenas',
    }
    # Manejo de formularios para añadir y editar ordenas
    if request.method == 'POST':
        if 'add_ordena' in request.POST:  # Si se pulsa el botón de Añadir Ordena
            ordena_form = OrdenaForm(request.POST)
            if ordena_form.is_valid():
                ordena_form.save()
                return redirect('ordenas')  # Redirige a la misma página

    else:
        ordena_form = OrdenaForm()
    # Si estamos editando una ordena, obtenemos esa ordena
    context['ordena_form'] = ordena_form
    html_template = loader.get_template('home/ordenas.html')
    return HttpResponse(html_template.render(context, request))
@login_required(login_url="/login/")

def eliminar_ordena(request, id_gasto):
    # Asegurarse de que la solicitud sea POST
    if request.method == 'POST':
        ordena = get_object_or_404(Ordena, id_gasto=id_gasto)
        ordena.delete()  # Elimina la ordena de la base de datos
    return redirect('ordenas')  # Redirige a la vista de ordenas



@login_required(login_url="/login/")
def compras_view(request):
    # BUSCAR COMPRAS
    search_query = request.GET.get('search', '')
    if search_query:
        compras = Compra.objects.filter(id_ingreso__icontains=search_query)
    else:
        compras = Compra.objects.all()
    context = {
        'compras': compras,
        'segment': 'compras',
    }
    # Manejo de formularios para añadir y editar compras
    if request.method == 'POST':
        if 'add_compra' in request.POST:  # Si se pulsa el botón de Añadir Compra
            compra_form = CompraForm(request.POST)
            if compra_form.is_valid():
                compra_form.save()
                return redirect('compras')  # Redirige a la misma página
    else:
        compra_form = CompraForm()
    # Si estamos editando una compra, obtenemos esa compra
    context['compra_form'] = compra_form
    html_template = loader.get_template('home/compras.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def eliminar_compra(request, id_ingreso):
    # Asegurarse de que la solicitud sea POST
    if request.method == 'POST':
        compra = get_object_or_404(Compra, id_ingreso=id_ingreso)
        compra.delete()  # Elimina la compra de la base de datos
    return redirect('compras')  # Redirige a la vista de compras