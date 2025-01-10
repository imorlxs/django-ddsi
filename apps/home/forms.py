from django import forms
from .models import Ingreso, Gasto, Campana, Empleado, Producto, Socio, Ordena, Compra, Genera  # Importa los modelos

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
        
class OrdenaForm(forms.Form):
    producto_id = forms.CharField(max_length=13, widget=forms.TextInput(attrs={'class': 'form-control'}))
    cantidad = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))

    def clean(self):
        cleaned_data = super().clean()
        producto_id = cleaned_data.get("producto_id")
        cantidad = cleaned_data.get("cantidad")

        if producto_id and cantidad:
            try:
                producto = Producto.objects.get(ID_producto=producto_id)
            except Producto.DoesNotExist:
                raise forms.ValidationError("Producto no encontrado")

            gasto = Gasto.objects.create(monto_gasto=producto.precio * cantidad)
            Ordena.objects.create(id_gasto=gasto)