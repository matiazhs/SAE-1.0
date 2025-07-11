# core/urls.py
from django.urls import path
from .views import UserProfileUpdateView, ConfiguracionEscolarUpdateView

from core.views import CustomLoginView, UserProfileUpdateView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('perfil/editar/', UserProfileUpdateView.as_view(), name='edit_profile'),
    path('perfil/config/', ConfiguracionEscolarUpdateView.as_view(), name='configuracion'),
]