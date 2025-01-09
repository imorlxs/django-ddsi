from django import forms
from .models import Ingreso, Gasto, Socio # Importa los modelos

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
            'motivo_bajaSocio',
            'fecha_bajaSocio',
        ]
        widgets = {
            'DNISocio': forms.TextInput(attrs={'class': 'form-control'}),
            'nombreSocio': forms.TextInput(attrs={'class': 'form-control'}),
            'apellidosSocio': forms.TextInput(attrs={'class': 'form-control'}),
            'emailSocio': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefonoSocio': forms.TextInput(attrs={'class': 'form-control'}),
            'direccionSocio': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_nacSocio': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'motivo_bajaSocio': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'fecha_bajaSocio': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
