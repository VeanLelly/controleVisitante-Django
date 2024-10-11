from django.db import models

class Apartamentos(models.Model):
    numero_apartamento = models.CharField(verbose_name='Número do apartamento', max_length=3)
    numero_bloco = models.CharField(verbose_name='Número do bloco', max_length= 1)
    vagas_estacionamento = models.CharField(verbose_name='Vagas no estacionamento', max_length= 2)


    class Meta:
            verbose_name = 'Apartamento'
            verbose_name_plural = 'Apartamentos'
            db_table = 'apartamento'

    

