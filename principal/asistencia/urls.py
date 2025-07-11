from django.urls import path # type: ignore

from .views import Asistencia_alumno_view, Asistencia_listado_view

urlpatterns = [
    
    path('asistencia/principal', Asistencia_listado_view.as_view(), name='asistencia_listado'),
    path('asistencia/<str:cuil>', Asistencia_alumno_view.as_view(), name='asistencia_alumno'),

]