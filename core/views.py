from django.forms import PasswordInput
from django.shortcuts import redirect, render
from .forms import ProductoForm, CustomUserForm
from .models import Producto
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login, authenticate
from .serializers import ProductoSerializer

# Rest_framework
from rest_framework import viewsets
from .serializers import ProductoSerializer

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
@permission_required('core.add_producto')
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
    

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer