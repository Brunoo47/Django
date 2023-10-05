from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Ocorrencias(models.Model):
    titulo = models.CharField(max_length=100)
    pacienteNome = models.CharField(max_length=100,blank=True, null=True)
    idade = models.IntegerField(blank=True, null=True)
    sexo = models.CharField(max_length=9, blank=True, null=True)
    cpfOrRg = models.CharField(max_length=11,blank=True, null=True)
    telefone = models.CharField(max_length=11, blank=True, null=True)
    acompanhanteNome = models.CharField(max_length=100, blank=True, null=True)
    acompanhanteIdade = models.IntegerField(blank=True, null=True)
    descricao = models.TextField()
    localOcorrencia = models.CharField(max_length=100)
    publicadoEm = models.DateTimeField(default=timezone.now)
    criadoPor  = models.ForeignKey(User,on_delete=models.CASCADE)
    equipe = models.CharField(max_length=100)

