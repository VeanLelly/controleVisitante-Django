from django.shortcuts import redirect,render
from django.contrib import messages
from visitantes.forms import VisitanteForm

def registrar_visitante (request):
    form = VisitanteForm()

    if request.method == 'POST':
        form = VisitanteForm(request.POST)

        if form.is_validad():
            visitante = form.save(commit=False)
            visitante.registrado_por = request.user.porteiro
            visitante = form.save

            messages.sucess(request,'Visitante registrado com sucesso!')
            return redirect('index')
        
    context = {
        'nome_pagina': 'Registrar Visitante',
        'form': form
    }

    return render(request, 'registrar_visitante.html', context)

# Create your views here.
