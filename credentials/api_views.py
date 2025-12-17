from rest_framework import viewsets
from .models import Issuer, Subject, Credential
from .serializers import IssuerSerializer, SubjectSerializer, CredentialSerializer

class IssuerViewSet(viewsets.ModelViewSet):
    queryset = Issuer.objects.all()
    serializer_class = IssuerSerializer

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class CredentialViewSet(viewsets.ModelViewSet):
    queryset = Credential.objects.all()
    serializer_class = CredentialSerializer
