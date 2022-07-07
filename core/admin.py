from django.contrib import admin
from core.models import Categoria, Producto

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'stock', 'cod.producto', 'categoria', 'marca' , 'precio']
    search_fields = ['nombre', 'cod.producto', 'marca']
    list_filter = ['categoria', 'marca', 'nombre']
    list_per_page: 10

admin.site.register(Producto)
admin.site.register(Categoria)