from django.urls import reverse_lazy  # type: ignore
from datetime import datetime, date
from .models import TipoAsistencia
from collections import defaultdict

from django.views.generic import ListView, UpdateView, DeleteView,CreateView, TemplateView, DetailView # type: ignore
from alumnos.views import Curso, Especialidad, Grupo

from .models import Asistencia, Alumno, TipoAsistencia


class Asistencia_listado_view(ListView):
    model = Alumno
    template_name = "asistencia_listado.html"
    context_object_name = "alumnos_con_asistencias"

    def get_queryset(self):
        queryset = Alumno.objects.select_related('curso', 'especialidad', 'grupo').all()
        
        curso = self.request.GET.get('curso')
        especialidad = self.request.GET.get('especialidad')
        grupo = self.request.GET.get('grupo')
        fecha = self.request.GET.get('fecha')

        if curso:
            queryset = queryset.filter(curso_id=curso)
        if especialidad:
            queryset = queryset.filter(especialidad_id=especialidad)
        if grupo:
            queryset = queryset.filter(grupo_id=grupo)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Obtenemos la fecha del filtro o usamos la actual
        fecha_filtro = self.request.GET.get('fecha')
        if fecha_filtro:
            fecha_filtro = datetime.strptime(fecha_filtro, '%Y-%m-%d').date()
        else:
            fecha_filtro = date.today()

        # Preparamos los datos de asistencias filtradas por fecha para cada alumno
        alumnos_con_asistencias = []
        for alumno in context['object_list']:
            # Filtramos las asistencias por la fecha seleccionada
            asistencias = alumno.asistencia_set.select_related('tipo').filter(fecha=fecha_filtro)
            
            alumno_data = {
                'alumno': alumno,
                'asistencias_agrupadas': []
            }
            
            if asistencias.exists():
                alumno_data['asistencias_agrupadas'].append({
                    'fecha': fecha_filtro,
                    'asistencias': asistencias,
                })
            
            alumnos_con_asistencias.append(alumno_data)
        
        context['alumnos_con_asistencias'] = alumnos_con_asistencias
        context['titulo'] = "Asistencia Alumnos"
        context['cursos'] = Curso.objects.all()
        context['especialidades'] = Especialidad.objects.all()
        context['grupos'] = Grupo.objects.all()
        context['tipos_asistencia'] = TipoAsistencia.objects.all()
        context['fecha_actual'] = fecha_filtro  # Usamos la fecha del filtro o la actual
        context['fecha_seleccionada'] = fecha_filtro.strftime('%Y-%m-%d')  # Para el input date
        
        return context

class Asistencia_alumno_view(ListView):
    model = Asistencia
    template_name = "asistencia_alumno.html"
    context_object_name = "asistencias"


    def get_queryset(self):
        return Asistencia.objects.filter(alumno__id=self.kwargs['cuil']).order_by('-fecha')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        alumno = Alumno.objects.get(id=self.kwargs['cuil'])
        context['alumno'] = alumno
        return context
