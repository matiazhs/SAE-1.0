from django.contrib import admin # type: ignore
from django.urls import path, include # type: ignore
from django.conf import settings # type: ignore
from django.conf.urls.static import static # type: ignore

from .views import PrincipalView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PrincipalView.as_view(), name='principal'),
    path('perfil/', PrincipalView.as_view(), name='principal'),


    # Esto incluirá las rutas de 'core/urls.py'
    path('perfil/', include('core.urls')),


    # Esto incluirá las rutas de 'alumnos/urls.py'
    path('alumnos/', include('alumnos.urls')),

    # Esto incluirá las rutas de 'asistencia/urls.py'
    path('asistencia/', include('asistencia.urls')),



] 
#+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


