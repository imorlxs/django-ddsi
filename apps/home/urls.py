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
 
    
    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),
    
    path('dar_de_alta_campaña/', views.dar_de_alta_campaña, name='dar_de_alta_campaña'),
    path('modificar_campaña/<int:campaign_id>/', views.modificar_campaña, name='modificar_campaña'),
    path('listar_campañas/', views.listar_campañas, name='marketing_lista_campañas'),
    path('eliminar_campaña/<int:campaign_id>/', views.eliminar_campaña, name='eliminar_campaña'),

]

