from django.db import models
from django.contrib.auth.models import User

class Endereco(models.Model):
    logradouro = models.CharField(max_length = 128)
    complemento = models.CharField(max_length = 256, null = True)
    uf = models.CharField(max_length = 2, null = True)
    cidade =  models.CharField(max_length = 64, null = True)
    cep = models.CharField(max_length = 10)

    def __str__(self):
        return '{},{},{}'.format(self.logradouro, self.cidade, self.uf)

class Pessoa(models.Model):
    nome = models.CharField(max_length=128)
    email = models.CharField(max_length=128)

    def __str__(self):
        return self.nome

class PessoaFisica(Pessoa):
    cpf = models.CharField(max_length = 12)

    def __str__(self):
        return self.cpf

class PessoaJuridica(Pessoa):
    cnpj = models.CharField(max_length = 100)
    razaoSocial = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.cnpj



class Eventos(models.Model):
    nome = models.CharField(max_length = 100)
    eventoPrincipal = models.CharField(max_length = 100)
    sigla = models.CharField(max_length = 10)
    dataEHoraDeInicio = models.DateField(max_length = 10)
    palavrasChaves = models.CharField(max_length = 100)
    logotipo = models.CharField(max_length = 10)
    realizador = models.ForeignKey('Pessoa',on_delete = models. PROTECT)
    endereco = models.ForeignKey ( 'Endereco' , on_delete = models. PROTECT)
    
    def __str__(self):
        return self.nome

class EventoCientifico(Eventos): 
    issn=models.CharField(max_length = 100)

    def __str__(self):
        return self.issn  


class Autor(Pessoa):
    curriculo = models.CharField(max_length = 100)
    #artigos = models.ManyToManyField('ArtigoCientifico')

class ArtigoCientifico(models.Model): 
    titulo =models.CharField(max_length = 100)
    autores = models.ManyToManyField('Autor')
    evento = models.ForeignKey('EventoCientifico',on_delete = models. PROTECT)


# Create your models here.
