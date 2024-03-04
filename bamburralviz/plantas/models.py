from django.db import models

class Planta(models.Model):

    nome_vulgar = models.CharField(max_length=100, null=False, blank=False)
    nome_cientifico = models.CharField(max_length=120, null=True, blank=True)
    familia = models.CharField(max_length=100, null=True, blank=True)
    reproducao = models.CharField(max_length=100, null=True, blank=True)
    floracao = models.CharField(max_length=100, null=True, blank=True)
    frutificacao = models.CharField(max_length=100, null=True, blank=True)
    uso = models.CharField(max_length=1000, null=True, blank=True) 
    caracteristica = models.CharField(max_length=1500, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=False)

