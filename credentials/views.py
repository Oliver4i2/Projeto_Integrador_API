from django.contrib.auth.views import LoginView as DjangoLoginView, LogoutView as DjangoLogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView
from .models import Credential, Issuer, Subject

# -------- AUTENTICAÇÃO --------
class LoginView(DjangoLoginView):
    """Tela de login usando autenticação padrão do Django."""
    template_name = 'login.html'


class LogoutView(DjangoLogoutView):
    """Logout simples, redireciona conforme settings.LOGOUT_REDIRECT_URL."""
    pass


# -------- DASHBOARD --------
class DashboardView(LoginRequiredMixin, TemplateView):
    """Dashboard com estatísticas gerais do sistema."""
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['total_credentials'] = Credential.objects.count()
        ctx['total_issuers'] = Issuer.objects.count()
        ctx['total_subjects'] = Subject.objects.count()

        # Top emissores e titulares (ordenados por quantidade de credenciais)
        ctx['top_issuers'] = Issuer.objects.annotate(num_credentials=models.Count('credentials')).order_by('-num_credentials')[:5]
        ctx['top_subjects'] = Subject.objects.annotate(num_credentials=models.Count('credentials')).order_by('-num_credentials')[:5]

        # Últimas credenciais emitidas
        ctx['latest_credentials'] = Credential.objects.select_related('issuer', 'subject').order_by('-timestamp')[:10]
        return ctx


# -------- CREDENTIAL --------
class CredentialListView(LoginRequiredMixin, ListView):
    """Lista de credenciais emitidas."""
    model = Credential
    template_name = 'credentials/list.html'
    context_object_name = 'credentials'
    paginate_by = 20


class CredentialDetailView(LoginRequiredMixin, DetailView):
    """Detalhe de uma credencial específica."""
    model = Credential
    template_name = 'credentials/detail.html'
    context_object_name = 'credential'


# -------- ISSUER --------
class IssuerListView(LoginRequiredMixin, ListView):
    """Lista de emissores cadastrados."""
    model = Issuer
    template_name = 'issuers/list.html'
    context_object_name = 'issuers'


# -------- SUBJECT --------
class SubjectListView(LoginRequiredMixin, ListView):
    """Lista de titulares cadastrados."""
    model = Subject
    template_name = 'subjects/list.html'
    context_object_name = 'subjects'
