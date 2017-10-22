from allauth.account.views import LoginView, PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView


class LoginView(LoginView):
    template_name = 'login_page.html'


class ChangePasswordView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'account/change_password.html'
    success_url = reverse_lazy('dashboard')


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'