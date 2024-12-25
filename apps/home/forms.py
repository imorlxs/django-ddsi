from django import forms
from .models import Ingreso, Gasto, Producto  # Importa los modelos

class IngresoForm(forms.ModelForm):
    class Meta:
        model = Ingreso
        fields = ['monto_ingreso']
        widgets = {
            'monto_ingreso': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class GastoForm(forms.ModelForm):
    class Meta:
        model = Gasto
        fields = ['monto_gasto']
        widgets = {
            'monto_gasto': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['ID_producto']  # Asegúrate de que el campo correcto esté en 'fields'
        widgets = {
            'ID_producto': forms.TextInput(attrs={'class': 'form-control'}),  # Cambiado a TextInput para el campo de texto
        }