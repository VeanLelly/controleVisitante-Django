from django.shortcuts import render
from django.utils import timezone
from visitantes.models import Visitante
from django.contrib.auth.decorators import login_required

@login_required
def index(request):

    todos_visitantes = Visitante.objects.order_by('-horario_chegada')

    visitante_arguardando = todos_visitantes.filter(status='ARGUARDANDO')
    visitante_em_visita = todos_visitantes.filter(status='EM_VISITA')
    visitante_finalizado = todos_visitantes.filter(status='FINALIZADO')

    hora_atual = timezone.now()
    mes_atual = hora_atual.month

    visitantes_mes = todos_visitantes.filter(horario_chegada__month = mes_atual)

    context = {
        'nome_pagina' : 'Inicio da Dashboard',
        'todos_visitantes' : todos_visitantes,
        'visitantes_mes' : todos_visitantes.count(),
        'visitante_arguardando': visitante_arguardando.count(),
        'visitante_em_visita' : visitante_em_visita.count(),
        'visitante_finalizado': visitante_finalizado.count(),
        'visitantes_mes' : visitantes_mes.count(),

    }
    return render(request, 'index.html', context)


