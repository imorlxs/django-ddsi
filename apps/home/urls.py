# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    
    #path('contabilidad', views.contabilidad_view, name='contabilidad'), 
    path('ingresos', views.ingresos_view, name='ingresos'),
    path('gastos', views.gastos_view, name='gastos'),
    path('contabilidad', views.contabilidad_view, name='contabilidad'),
    path('eliminar_ingreso/<int:ingreso_id>/', views.eliminar_ingreso, name='eliminar_ingreso'),   
    path('eliminar_gasto/<int:gasto_id>/', views.eliminar_gasto, name='eliminar_gasto'),    
 
    
    path('campanas', views.campanas_view, name='campanas'),  # Vista principal de campañas
    path('eliminar_campana/<int:id_campana>/', views.eliminar_campana, name='eliminar_campana'),  # Eliminar campaña

    path('empleados', views.empleados_view, name='empleados'),  # Vista principal de empleados
    path('eliminar_empleado/<str:DNIEmpleado>/', views.eliminar_empleado, name='eliminar_empleado'),  # Eliminar empleado
    
    #productos
    path('productos', views.productos_view, name='productos'),
    path('eliminar_producto/<str:ID_producto>/', views.eliminar_producto, name='eliminar_producto'),
    
    path('socios', views.socios_view, name='socios'),  # Vista principal de socios
    path('eliminar_socio/<str:DNISocio>/', views.eliminar_socio, name='eliminar_socio'),  # Eliminar socio

    path('ordenas', views.ordenar_view, name='ordenas'),
    path('eliminar_ordena/<int:ordena_id>/', views.eliminar_ordena, name='eliminar_ordena'),
    
    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),
    
    

]

