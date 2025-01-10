from django import forms
from .models import Ingreso, Gasto, Campana, Empleado, Producto, Socio, Ordena, Compra, Genera  # Importa los modelos
from django.utils import timezone

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
        
    def save(self, commit=True):
        instance = super().save(commit=False)
        
        gasto = Gasto.objects.create(monto_gasto=instance.precio)
       
        
        if commit:
            instance.save()
            Genera.objects.create(id_campana=instance, id_gasto=gasto, fecha_genera=timezone.now().date())
            
        return instance
        

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
        
class SocioForm(forms.ModelForm):
    class Meta:
        model = Socio
        fields = [
            'DNISocio',
            'nombreSocio',
            'apellidosSocio',
            'emailSocio',
            'telefonoSocio',
            'direccionSocio',
            'fecha_nacSocio',
        ]
        widgets = {
            'DNISocio': forms.TextInput(attrs={'class': 'form-control'}),
            'nombreSocio': forms.TextInput(attrs={'class': 'form-control'}),
            'apellidosSocio': forms.TextInput(attrs={'class': 'form-control'}),
            'emailSocio': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefonoSocio': forms.TextInput(attrs={'class': 'form-control'}),
            'direccionSocio': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_nacSocio': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
        
class OrdenaForm(forms.ModelForm):
    class Meta:
        model = Ordena
        fields = ['id_producto', 'id_empleado', 'cantidad']
        widgets = {
            'id_producto': forms.Select(attrs={'class': 'form-control'}),
            'id_empleado': forms.Select(attrs={'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
        }
    
    def save(self, commit=True):
        instance = super().save(commit=False)
        producto = instance.id_producto
        cantidad = instance.cantidad
        monto_gasto = producto.precio * cantidad
    
        gasto = Gasto.objects.create(monto_gasto=monto_gasto)
        instance.id_gasto = gasto
      
        instance.fecha_gasto = timezone.now().date()
        instance.hora_gasto = timezone.now()
    
        if commit:
            instance.save()
            producto.cantidad += cantidad
            producto.save()
        return instance

class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = ['id_producto', 'dnisocio', 'cantidad']
        widgets = {
            'id_producto': forms.Select(attrs={'class': 'form-control'}),
            'dnisocio': forms.Select(attrs={'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        
    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.fecha_compra = timezone.now().date()
        ingreso = Ingreso.objects.create(monto_ingreso=instance.id_producto.precio * instance.cantidad)
        instance.id_ingreso = ingreso

        if commit:
            instance.save()
            producto = instance.id_producto
            producto.cantidad -= instance.cantidad
            producto.save()
        return instance
