from django import forms
from .models import Ingreso, Gasto, Campana, Empleado, Producto  # Importa los modelos

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

class CampanaForm(forms.ModelForm):
    class Meta:
        model = Campana
        fields = ['id_campana', 'nombre_campana', 'tipo', 'estado', 'precio']
        widgets = {
            'id_campana': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre_campana': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['DNIEmpleado', 'nombreEmpleado', 'apellidosEmpleado', 'cargo', 
                 'telefonoEmpleado', 'emailEmpleado', 'direccionEmpleado', 
                 'fecha_nacEmpleado']
        widgets = {
            'DNIEmpleado': forms.TextInput(attrs={'class': 'form-control'}),
            'nombreEmpleado': forms.TextInput(attrs={'class': 'form-control'}),
            'apellidosEmpleado': forms.TextInput(attrs={'class': 'form-control'}),
            'cargo': forms.TextInput(attrs={'class': 'form-control'}),
            'telefonoEmpleado': forms.TextInput(attrs={'class': 'form-control'}),
            'emailEmpleado': forms.EmailInput(attrs={'class': 'form-control'}),
            'direccionEmpleado': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_nacEmpleado': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
        
class ProductoForm(forms.ModelForm):    
    class Meta:
        model = Producto
        fields = ['ID_producto', 'nombre_producto', 'cantidad', 'precio', 'tallas', 'proveedor']
        widgets = {
            'ID_producto': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre_producto': forms.TextInput(attrs={'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'tallas': forms.TextInput(attrs={'class': 'form-control'}),
            'proveedor': forms.TextInput(attrs={'class': 'form-control'}),
        }