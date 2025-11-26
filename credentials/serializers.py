from rest_framework import serializers
from .models import Issuer, Credential

class IssuerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issuer
        fields = '__all__'

class CredentialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Credential
        fields = '__all__'
        read_only_fields = ['hash', 'issued_at']
