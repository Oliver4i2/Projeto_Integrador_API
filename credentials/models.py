from django.db import models
from django.utils import timezone


class Issuer(models.Model):
    """Entidade emissora de credenciais (ex: universidade, órgão público)."""
    name = models.CharField(max_length=255)
    did = models.CharField(max_length=255, unique=True)  # Decentralized Identifier

    def __str__(self):
        return self.name


class Subject(models.Model):
    """Titular da credencial (ex: estudante, cidadão)."""
    name = models.CharField(max_length=255)
    did = models.CharField(max_length=255, unique=True)  # Identificador descentralizado

    def __str__(self):
        return self.name


class Credential(models.Model):
    """Credencial emitida e registrada na blockchain."""
    issuer = models.ForeignKey(Issuer, on_delete=models.PROTECT, related_name='credentials')
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT, related_name='credentials')
    type = models.CharField(max_length=100, default="credential")  # Tipo da credencial (ex: diploma, identidade)
    data = models.JSONField()  # Dados da credencial
    hash = models.CharField(max_length=64, editable=False)  # Hash SHA-256
    timestamp = models.DateTimeField(auto_now_add=True)  # Registro de criação

    def __str__(self):
        return f'{self.type} - {self.subject.name}'
