from django.db import models

class Issuer(models.Model):
    name = models.CharField(max_length=255)
    did = models.CharField(max_length=255, unique=True)  # Decentralized Identifier
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Credential(models.Model):
    issuer = models.ForeignKey(Issuer, on_delete=models.CASCADE)
    subject_did = models.CharField(max_length=255)  # DID do cidadão
    credential_type = models.CharField(max_length=100)
    data = models.JSONField()
    hash = models.CharField(max_length=64, unique=True)
    issued_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.credential_type} for {self.subject_did}"
