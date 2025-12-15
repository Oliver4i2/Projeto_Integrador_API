from django.urls import path
from .views import (
    IssuerListCreateView, IssuerDetailView,
    SubjectListCreateView, SubjectDetailView,
    CredentialListCreateView, CredentialDetailView
)

urlpatterns = [
    # Subjects
    path('subjects/', SubjectListCreateView.as_view(), name='subject-list-create'),
    path('subjects/<int:pk>/', SubjectDetailView.as_view(), name='subject-detail'),

    # Issuers
    path('issuers/', IssuerListCreateView.as_view(), name='issuer-list-create'),
    path('issuers/<int:pk>/', IssuerDetailView.as_view(), name='issuer-detail'),

    # Credentials
    path('credentials/', CredentialListCreateView.as_view(), name='credential-list-create'),
    path('credentials/<int:pk>/', CredentialDetailView.as_view(), name='credential-detail'),
]
