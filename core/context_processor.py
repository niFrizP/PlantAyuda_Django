import re


def total_carro(request):
    total = 0
    if request.user.is_authenticated:
        if request.session('carro'):
            for key, Value in request.session['carro'].items():
                total+= int(Value['acumulado'])
    return{'total_carro': total}