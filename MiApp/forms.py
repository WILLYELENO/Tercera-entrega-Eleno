from django import forms
from MiApp.models import Compra, Proveedor, Producto

class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = '__all__'

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = '__all__'

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'