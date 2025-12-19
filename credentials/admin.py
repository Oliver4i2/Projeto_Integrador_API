from django.contrib import admin
from .models import Issuer, Subject, Credential

@admin.register(Issuer)
class IssuerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'did')

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'did')

@admin.register(Credential)
class CredentialAdmin(admin.ModelAdmin):
    list_display = ('id', 'credential_type', 'issuer', 'subject', 'hash')
