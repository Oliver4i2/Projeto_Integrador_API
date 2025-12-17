from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import IssuerViewSet, SubjectViewSet, CredentialViewSet
from .views import (
    CredentialListView,
    CredentialDetailView,
    IssuerListView,
    SubjectListView,
    DashboardView,
)

router = DefaultRouter()
router.register(r'issuers', IssuerViewSet)
router.register(r'subjects', SubjectViewSet)
router.register(r'credentials', CredentialViewSet)

urlpatterns = [
    # HTML views
    path('credentials/', CredentialListView.as_view(), name='credentials-list'),
    path('credentials/<int:pk>/', CredentialDetailView.as_view(), name='credentials-detail'),
    path('issuers/', IssuerListView.as_view(), name='issuers-list'),
    path('subjects/', SubjectListView.as_view(), name='subjects-list'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),

    # API endpoints
    path('api/', include(router.urls)),
]
