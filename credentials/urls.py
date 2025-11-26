from django.urls import path
from .views import IssuerView, CredentialView, SubjectView

urlpatterns = [
    path('issuers/', IssuerView.as_view(), name='issuer'),
    path('credentials/', CredentialView.as_view(), name='credential'),
    path('subjects/', SubjectView.as_view(), name='subject'),
]
