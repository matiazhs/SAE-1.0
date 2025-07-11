from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from .models import UserProfile, ConfiguracionEscolar
from django.shortcuts import redirect
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from core.forms import UserProfileForm, ConfiguracionEscolarForm
from django.shortcuts import render



class CustomLoginView(LoginView):
    template_name = 'login.html'

    def get_success_url(self):
        return reverse_lazy('principal')

class UserProfileUpdateView(UpdateView):

    model = UserProfile
    form_class = UserProfileForm
    template_name = 'edit_profil.html'
    success_url = '/'

    def get_object(self):
        perfil, creado = UserProfile.objects.get_or_create(user=self.request.user)
        return perfil
    
class ConfiguracionEscolarUpdateView(UpdateView):
    model = ConfiguracionEscolar
    form_class = ConfiguracionEscolarForm
    template_name = 'configuracion_escolar_form.html'
    success_url = reverse_lazy('principal')

    def get_object(self, queryset=None):
        return ConfiguracionEscolar.load()  # Carga la única instancia
