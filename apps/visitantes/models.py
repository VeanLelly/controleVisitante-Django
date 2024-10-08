from django.db import models

# Create your models here.
STATUS_VISITANTE=[
    ('AGUARDANDO', 'Aguardando Autorização'),
    ('EM_VISITA', 'Em visita'),
    ('FINALIZADO', 'Visita finalizada')
]
class Visitante(models.Model):
    status = models.CharField(verbose_name='status',choices=STATUS_VISITANTE, max_length=10, default='AGUARDANDO')
    nome_completo = models.CharField(verbose_name='Nome completo', max_length=200)
    cpf = models.CharField(verbose_name='CPF', max_length=11)
    telefone = models.CharField(verbose_name='Telefone', max_length=11)
    data_Nascimento = models.DateField(verbose_name='Data de nascimento', auto_now=False, auto_now_add=False)
    numero_casa = models.PositiveSmallIntegerField(verbose_name='número da casa a ser visitada')
    placa_veiculo = models.CharField(verbose_name='placa do carro', max_length=7, blank=True, null=True)
    horario_chegada = models.DateTimeField(verbose_name='horario chegada na portaria', auto_now_add=True)
    horario_autorizacao = models.DateTimeField(verbose_name='horario da autorizacao de entrada', auto_now_add=False, blank=True, null=True)
    horario_saida = models.DateTimeField(verbose_name='horario saida na portaria', auto_now_add=False, blank=True, null=True)
    morador_responsavel = models.CharField(verbose_name='nome do morador responsavel', max_length=100, blank=False, null=False)
    registrado_por = models.ForeignKey('porteiros.Porteiro', verbose_name='Porteiro responsavel pela registro', on_delete=models.PROTECT)

    def get_horario_saida(self):
        if self.horario_saida:
            return self.horario_saida
            
    def get_horario_autorizacao(self):
        if self.horario_autorizacao:
            return self.horario_autorizacao
    
    def get_morador_responsavel(self):
        if self.morador_responsavel:
            return self.morador_responsavel
        
    def get_placa_veiculo(self):
        if self.placa_veiculo:
            return self.placa_veiculo
        
    def get_cpf(self):
        if self.cpf:
            cpf = str(self.cpf)

            cpf_parte_um = cpf[0:3]
            cpf_parte_dois = cpf[3:6]
            cpf_parte_tres = cpf[6:9]
            cpf_parte_quartro = cpf[9:11]

            cpf_formatado = f'{cpf_parte_um}.{cpf_parte_dois}.{cpf_parte_tres}-{cpf_parte_quartro}'
            return cpf_formatado
        
    class Meta:
            verbose_name = 'Visitante'
            verbose_name_plural = 'Visitantes'
            db_table = 'visitante'

    def __str__(self):
        return self.nome_completo
    
    
    
