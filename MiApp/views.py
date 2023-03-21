from django.shortcuts import render
from MiApp.forms import CompraForm, ProveedorForm, ProductoForm
from MiApp.models import Proveedor


# Create your views here.

def base (request):
    return render(request, "MiApp/base.html")

def index (request):
    return render(request, "MiApp/index.html")

def compras (request):
    context = {"form":CompraForm(),}
    return render(request, "MiApp/compras.html", context)

def agregar_compra (request):
    compra_form = CompraForm(request.POST)
    compra_form.save()
    context = {"form":CompraForm(),}
    return render(request, "MiApp/compras.html", context)

def proveedores (request):
    context = {"form":ProveedorForm(),}
    return render(request, "MiApp/proveedores.html", context)

def agregar_proveedor (request):
    proveedor_form = ProveedorForm(request.POST)
    proveedor_form.save()
    context = {"form":ProveedorForm(),}
    return render(request, "MiApp/proveedores.html", context)

def productos (request):
    context = {"form":ProductoForm(),}
    return render(request, "MiApp/productos.html",context)

def agregar_producto (request):
    recurso_form = ProductoForm(request.POST)
    recurso_form.save()
    context = {"form":ProductoForm(),}
    return render(request, "MiApp/recursos.html", context)
    
def buscar_proveedor (request):
    criterio = request.GET.get("criterio")
    context = {
        "proveedor": Proveedor.objects.filter(nombre__icontains=criterio).all(),
    }
    return render (request, "MiApp/proveedores.html", context)