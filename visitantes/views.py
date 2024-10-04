from django.shortcuts import get_object_or_404, redirect,render
from django.contrib import messages
from visitantes.forms import VisitanteForm
from django.contrib.auth.decorators import login_required

from visitantes.models import Visitante


@login_required

def registrar_visitante (request):
    form = VisitanteForm()

    if request.method == 'POST':
        form = VisitanteForm(request.POST)

        if form.is_valid():
            visitante = form.save(commit=False)
            visitante.registrado_por = request.user.porteiro
            visitante = form.save

            messages.success(request,'Visitante registrado com sucesso!')
            return redirect('index')
        
    context = {
        'nome_pagina': 'Registrar Visitante',
        'form': form
    }

    return render(request, 'registrar_visitante.html', context)



def informacoes_visitante (request,pk):
    informacoesVisitante = get_object_or_404(Visitante, pk=pk)
    context = {
        'nome_pagina': 'informacoes_visitante',
        'informacoes_visitante': informacoesVisitante
    }

    return render(request, 'informacoes_visitante.html', context)






# Create your views here
