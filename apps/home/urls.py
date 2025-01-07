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
 
    
    #Ruta para empleados
    path('', views.listar_empleados, name='listar_empleados'),
    path('registrar/', views.registrar_empleado, name='registrar_empleado'),
    path('modificar/<int:empleado_id>/', views.modificar_empleado, name='modificar_empleado'),
    path('consultar/<int:empleado_id>/', views.consultar_empleado, name='consultar_empleado'),
    path('eliminar/<int:empleado_id>/', views.eliminar_empleado, name='eliminar_empleado'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),
    
]
