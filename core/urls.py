from django import urls
from django.contrib import admin
from xml.etree.ElementInclude import include
from django.urls import URLPattern, path
from .views import home, arbustos, contacto, flores, jardineria, login, macetero, productos, registro, tierrahoja, listadoproductos, insertarproductos, modificarproductos, eliminar_producto

urlpatterns =[
    path('',home,name="home"),
    path('arbustos/',arbustos,name="arbustos"),
    path('contacto/',contacto,name="contacto"),
    path('flores/',flores,name="flores"),
    path('jardineria/',jardineria,name="jardineria"),
    path('login/',login,name="login"),
    path('macetero/',macetero,name="macetero"),
    path('productos/',productos,name="productos"),
    path('registro/', registro,name="registro"),
    path('tierrahoja/',tierrahoja,name="tierrahoja"),
    path('listadoproductos/', listadoproductos, name="listadoproductos"),
    path('insertarproductos/', insertarproductos, name="insertarproductos"),
    path('modificarproductos/<id>/', modificarproductos, name="modificarproductos"),
    path('eliminar_producto/<id>/', eliminar_producto,name="eliminar_producto"),

]

