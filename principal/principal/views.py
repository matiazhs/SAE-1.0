from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from core.views import ConfiguracionEscolar

from django.views.generic import TemplateView, UpdateView

from django.urls import reverse_lazy

class PrincipalView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Agregá cualquier dato que quieras pasar al template

        # Cargar la configuración escolar
        config = ConfiguracionEscolar.load()

        context['titulo'] = 'Sistema de Administracion Escolar (S.A.E)'

        context['datos_escuela'] = {
            'nombre_escuela': config.nombre_escuela,
            'cue': config.cue,
            'distrito': config.distrito,
            'sector_gestion': config.sector_gestion,
            'numero': config.numero,
            'clave_provincial': config.clave_provincial
        }

        return context
    
