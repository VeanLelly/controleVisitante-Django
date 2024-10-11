from django.shortcuts import redirect, render
from .models import Moradores



def lista_moradores(request):

    moradores = Moradores.objects.order_by(request)

    if request.method == 'POST':
        moradores = Moradores(request.POST)
       
        context = {
            'nome_pagina': 'Lista dos Moradores',
            'nome_morador' : moradores,
            'contato' : moradores,
   }

    return render(request, 'lista_moradores.html', context)