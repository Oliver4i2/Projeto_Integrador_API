from django.db import models

class Issuer(models.Model):
    name = models.CharField(max_length=255)
    did = models.CharField(max_length=255, unique=True)  # Decentralized Identifier
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Credential(models.Model):
    issuer = models.ForeignKey('Issuer', on_delete=models.CASCADE, related_name='credentials')
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE, related_name='credentials', null=True, blank=True)
    credential_type = models.CharField(max_length=255)
    data = models.JSONField()
    hash = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.credential_type} - {self.subject.did}"


class Subject(models.Model):
    did = models.CharField(max_length=255, unique=True)  # identificador descentralizado
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.did})"