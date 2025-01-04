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
    
    #productos
    path('productos', views.productos_view, name='produsctos'),
    path('eliminar_producto/<int:ID_producto>/', views.eliminar_producto, name='eliminar_producto'),   


 
    
    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),
    
]
#aniadir la ruta de donde esta la ruta de la vista, cada funcion lleva su nombre