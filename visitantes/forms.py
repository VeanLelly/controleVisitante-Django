from django import forms
from .models import Visitante
from typing_extensions import Required

class VisitanteForm(forms.ModelForm):

    class Meta:
        model = Visitante
        fields = [
            'nome_completo', 'cpf', 'data_Nascimento', 'numero_casa', 'placa_veiculo',
        ]
        error_menssages = {
            'nome_completo':{'required': 'O nome completo do visitante é obrigatório para o registro.'
            },
            'cpf':{'required': 'O cpf do visitante é obrigatório para o registro'},
            'data_Nascimento':{'required':'A data de nascimento do visitante é obrigatório para o registro'},
            'numero_casa':{'required': 'O número da casa a ser visitada é obrigatório para o registro'},
        }

    class AutorizaVisitanteForm(forms.ModelForm):
        class Meta:
            model = Visitante
            fields = [
            'morador_responsavel'
            ]
            error_menssage ={
                'morador_responsavel':{
                    'required': 'Por favor, informe o nome do morador que receberá sua visita'
                }
            }

