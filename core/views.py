from django.forms import PasswordInput
from django.shortcuts import redirect, render
from core.forms import ProductoForm
from core.models import Producto
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from .forms import CustomUserForm
from .forms import ProductoForm

# Create your views here.
def home(request):
    return render(request,'core/home.html')
def arbustos(request):
    return render(request,'core/arbustos.html')
def contacto(request):
    return render(request,'core/contacto.html')
def flores(request):
    return render(request,'core/flores.html')
def jardineria(request):
    return render(request,'core/jardineria.html')
def login(request):
    return render(request,'core/templates/registration/login.html')
def macetero(request):
    return render(request,'core/macetero.html')
def productos(request):
    return render(request,'core/productos.html')
def registro(request):
    data = {
        'form' :CustomUserForm()
    }
    if request.method == 'POST':
        formulario = CustomUserForm(request.POST)
        if formulario.is_valid():
            formulario.save();
            username = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
        return redirect(to='home')  
    return render(request, 'registration/registro.html', data)

def tierrahoja(request):
    return render(request,'core/tierrahoja.html')
def listadoproductos(request):
    productos = Producto.objects.all()
    data = {
        'producto':productos
    }
    return render(request,'core/Inventario/listadoproductos.html', data)

    return render(request, 'core/inventario/insertarproductos.html',data)
def modificarproductos(request, id):
    productos = Producto.objects.get(id=id)
    data = {
        'form':ProductoForm(instance=Producto)
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=Producto)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Modificado Correctamente"
            data['form'] = formulario
    return render(request, 'core/inventario/modificarproductos.html', data)
def eliminar_producto(request, id):
    Producto = Producto.objects.get(id=id)
    Producto.delete()

    return redirect(to="listadoproductos")
@login_required
def insertarproductos(request):
    data={
        'form':ProductoForm()
    }
    if request.method == 'POST':
        formulario = ProductoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Añadido Exitosamente!"
    return render(request, 'core/Inventario/insertarproductos.html' ,data)