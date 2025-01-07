from django import forms
from .models import Ingreso, Gasto  # Importa los modelos
from .models import Empleado

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



class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'