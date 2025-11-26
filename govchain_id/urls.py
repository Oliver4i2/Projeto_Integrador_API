from django.urls import path
from .views import IssuerView, CredentialView

urlpatterns = [
    path('issuers/', IssuerView.as_view(), name='issuer'),
    path('credentials/', CredentialView.as_view(), name='credential'),
]
