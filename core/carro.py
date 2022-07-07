from tkinter import SEL_FIRST
from typing_extensions import Self

class carro:
    def __init__(self, request):
        self.request = request
        self.request = request.session
        carro = self.session['carro']
        if not carro:
            self.session['carro'] = {}
            self.carro = self.session["carro"]
        else:
            self.carro = carro
    
    def agregar(self, producto):
        id = str(producto.id)
        if id not in self.carro.key():
            self.carro[id]={
                "producto_id":producto.id,
                "nombre":producto.nombre,
                "precio":producto.precio,
                "cantidad":1,
            }
        else:
            self.carro[id]['cantidad']+=1
            self.carro[id]['acumulado']+= producto.precio
        self.guardar_carro()

    def guardar_carro(self):
        self.session['carro']=self.carro
        self.session.modified = True

    def eliminar(self, producto):
        id = str(producto.id)
        if id in self.carro:
            del self.carro[id]
            self.guardar_carro()

    def restar(self, producto):
        id = str(producto.id)
        if id in self.carro.keys():
            self.carro[id]['cantidad']-=1
            self.carro[id]['acumulado']-= producto.precio
            if self.carrito[id]['cantidad']<=0: self.eliminar(producto)
            self.guardar_carro()

    def limpiar(self):
        self.session['carro'] = {}
        self.session.modified = True