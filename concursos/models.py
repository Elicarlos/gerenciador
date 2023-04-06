from django.db import models
from django.contrib.auth.models import User
from django_tenants.models import TenantMixin, DomainMixin


class Client(TenantMixin):
    name = models.CharField(max_length=100)
    paid_until = models.CharField(max_length=100)
    on_trial = models.BooleanField()
    created_on = models.DateField(auto_now_add=True)

    # specify the database schema to use for this tenant
    auto_create_schema = True

class MyDomain(DomainMixin):
    pass

class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    
    def __str__(self):
        return self.nome

class Concurso(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    data_inicio = models.DateField()
    data_fim = models.DateField()
    
    def __str__(self):
        return self.titulo

class Participante(models.Model):
    concurso = models.ForeignKey(Concurso, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    cpf = models.CharField(max_length=14)
    
    def __str__(self):
        return self.nome
