from django.http import HttpResponseNotAllowed
from django.utils import timezone
from django.shortcuts import get_object_or_404, redirect,render
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import VisitanteForm, AutorizaVisitanteForm
from .models import Visitante


@login_required

def registrar_visitante (request):
    form = VisitanteForm()

    if request.method == 'POST':
        form = VisitanteForm(request.POST)

        if form.is_valid():
            visitante = form.save(commit=False)
            visitante.registrado_por = request.user.porteiro
            visitante = form.save()

            messages.success(request,'Visitante registrado com sucesso!')
            return redirect('index')
        
    context = {
        'nome_pagina': 'Registrar Visitante',
        'form': form
    }

    return render(request, 'registrar_visitante.html', context)



def informacoes_visitante (request,pk):
    visitante = get_object_or_404(Visitante, pk=pk)

    form = AutorizaVisitanteForm(request.POST, instance= visitante)
    if form.is_valid():
        visitante = form.save(commit=False)
        visitante.status = 'EM_VISITA'
        visitante.horario_autorizacao = timezone.now()

        visitante.save()

        messages.success(request, 'Entrada de visitante autorizada com sucesso!')

        return redirect('index')

    context = {
        'nome_pagina': 'Informações dos Visitantes',
        'informacoes_visitante': visitante,
        'form':form,
    }

    return render(request, 'informacoes_visitante.html', context)

@login_required
def finalizar_visita(request, pk):

    if request.method == 'POST':
        visitante = get_object_or_404(Visitante,pk=pk)
        visitante.status = 'FINALIZADO'
        visitante.horario_saida = timezone.now()
        visitante.save()

        messages.success(request, 'Entrada de visitante autorizada com sucesso!')
        return redirect('index')
    else:
        return HttpResponseNotAllowed(['POST'], 'Método não permitido')

    
   







# Create your views here
