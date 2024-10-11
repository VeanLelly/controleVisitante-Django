from django.db import models

class Moradores(models.Model):
    nome_morador = models.CharField(verbose_name='Nome do morador', max_length=200)
    contato = models.CharField(verbose_name='Contado do morador', max_length= 11)
    
    class Meta:
            verbose_name = 'Morador'
            verbose_name_plural = 'Moradores'
            db_table = 'morador'

   
    def __str__(self):
        return self.nome_morador
    


