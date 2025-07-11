from django.contrib import messages # type: ignore
from openpyxl import load_workbook # type: ignore
from django.shortcuts import render, redirect, get_object_or_404 # type: ignore
from django.urls import reverse_lazy  # type: ignore
from datetime import datetime
from django.db.models import Prefetch # type: ignore
from django.http import JsonResponse # type: ignore
from django.contrib.messages.views import SuccessMessageMixin # type: ignore
from django.contrib.auth.mixins import LoginRequiredMixin # type: ignore
from django.core.exceptions import ValidationError # type: ignore
from django.views import View  # type: ignore

from .models import Alumno, Docente, AlumnoDatos, Curso, Especialidad, GrupoMateria, Grupo, Turno, Materia, TipoCargo, Cargo
from .forms import AlumnoForm, AlumnoDatosForm, AlumnoUploadFileForm, EspecialidadForm, TurnoForm, CursoForm, DocenteForm, GrupoForm, MateriaForm, GrupoMateriaForm, CargoForm
from django.views.generic import ListView, UpdateView, DeleteView,CreateView, TemplateView, DetailView # type: ignore



# ALUMNO

class Alumnos_listado_view(LoginRequiredMixin, ListView):
    model = Alumno
    template_name = "alumnos_listado.html"
    success_url = reverse_lazy('listado_alumnos')
    
    def get_queryset(self):
        # Optimizamos la consulta con select_related
        return super().get_queryset().select_related('curso', 'especialidad')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Agregamos los datos para los filtros
        context["titulo"] = "Listado de Alumnos"
        context["cursos"] = Curso.objects.filter(alumnos__isnull=False).distinct()
        context["especialidades"] = Especialidad.objects.filter(alumnos__isnull=False).distinct()
        
        return context
    
class AlumnoUpdateView(UpdateView):
    model = Alumno
    form_class = AlumnoForm
    template_name = 'editar_alumno.html'
    context_object_name = 'alumno'

    # Establecer el URL de redirección después de una actualización exitosa
    def get_success_url(self):
        return reverse_lazy('alumnos_listado')  # Redirige al listado de alumnos después de la actualización

    # Este método se utiliza para obtener el objeto del alumno basado en el cuil
    def get_object(self, queryset=None):
        cuil = self.kwargs['cuil']
        return Alumno.objects.get(cuil=cuil)

class AlumnoDeleteView(DeleteView):
    model = Alumno
    template_name = 'eliminar_alumno.html'
    success_url = reverse_lazy('alumnos_listado')

    def get_object(self, queryset=None):
        return Alumno.objects.get(cuil=self.kwargs['cuil'])

class AlumnoCreateView(CreateView):
    model = Alumno
    form_class = AlumnoForm
    template_name = 'alta_alumno.html' 
    success_url = reverse_lazy('alumnos_listado') 
    
    def form_valid(self, form):
        return super().form_valid(form)

class AlumnoDatosView(CreateView):
    model = AlumnoDatos
    form_class = AlumnoDatosForm
    template_name = "datos_alumno.html"
    success_url = reverse_lazy('alumnos_listado')  # Redirige a la misma URL después del envío

    def form_valid(self, form):
        return super().form_valid(form)
    
class AlumnoDatosCUILView(UpdateView):
    model = AlumnoDatos
    form_class = AlumnoDatosForm
    template_name = 'datos_alumno.html'
    success_url = reverse_lazy('alumnos_listado')

    def get_object(self, queryset=None):
        cuil = self.kwargs.get('cuil')
        if cuil:
            obj, created = AlumnoDatos.objects.get_or_create(cuil=cuil)
            return obj
        return None

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if 'instance' in kwargs and kwargs['instance']:
            # Verificar y formatear fecha_nacimiento
            if hasattr(kwargs['instance'], 'fecha_nacimiento') and kwargs['instance'].fecha_nacimiento:
                fecha = kwargs['instance'].fecha_nacimiento
                # Si es string (ej: "12/01/1982"), convertirlo a objeto date
                if isinstance(fecha, str):
                    try:
                        fecha_obj = datetime.strptime(fecha, '%d/%m/%Y').date()
                        kwargs['initial'] = {'fecha_nacimiento': fecha_obj.strftime('%Y-%m-%d')}
                    except ValueError:
                        pass
                # Si ya es objeto date, formatear a YYYY-MM-DD
                elif hasattr(fecha, 'strftime'):
                    kwargs['initial'] = {'fecha_nacimiento': fecha.strftime('%Y-%m-%d')}
        return kwargs

    def dispatch(self, request, *args, **kwargs):
        if not self.kwargs.get('cuil'):
            return redirect('alumnos_listado')
        return super().dispatch(request, *args, **kwargs)
    

# DOCENTE

class Docentes_listado_view(ListView):
    model = Docente
    template_name = 'docentes_listado.html'
    context_object_name = 'docentes'
    
    def get_queryset(self):
        # Optimización de consultas con prefetch_related
        queryset = super().get_queryset()
        return queryset.prefetch_related(
            Prefetch(
                'carga_academica',
                queryset=GrupoMateria.objects.select_related(
                    'materia', 'grupo', 'materia__curso'
                )
            )
        ).order_by('apellido', 'nombre')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Listado de Docentes"
        return context

class DocenteUpdateView(UpdateView):
    model = Docente
    form_class = DocenteForm
    template_name = 'editar_docente.html'
    context_object_name = 'docente'

    # Establecer el URL de redirección después de una actualización exitosa
    def get_success_url(self):
        return reverse_lazy('docentes_listado')  # Redirige al listado de alumnos después de la actualización

    # Este método se utiliza para obtener el objeto del alumno basado en el cuil
    def get_object(self, queryset=None):
        cuil = self.kwargs['cuil']
        return Docente.objects.get(cuil=cuil)

class DocenteDeleteView(DeleteView):
    model = Docente
    template_name = 'eliminar_docente.html' 
    success_url = reverse_lazy('docentes_listado')

    def get_object(self, queryset=None):
        return Docente.objects.get(cuil=self.kwargs['cuil'])

class DocenteMateriasView(View):
    def get(self, request, pk):
        docente = Docente.objects.prefetch_related(
            Prefetch(
                'carga_academica',
                queryset=GrupoMateria.objects.select_related(
                    'materia', 'grupo', 'materia__curso'
                )
            )
        ).get(pk=pk)
        
        data = []
        for asignacion in docente.carga_academica.all():
            data.append({
                'materia': 
                {
                    'nombre': asignacion.materia.nombre,
                    'tipo': asignacion.materia.tipo,
                    'pid': asignacion.materia.pid,
                    'cupof': asignacion.materia.cupof,
                    'fecha_toma_posesion': asignacion.materia.fecha_toma_posesion,
                    'forma_ingreso': asignacion.materia.forma_ingreso,
                    'numero_dispo': asignacion.materia.numero_dispo,
                    'secuencia': asignacion.materia.secuencia,
                    'horario_inicio': asignacion.materia.horario_inicio,
                    'horario_fin': asignacion.materia.horario_fin,
                    'dias_semana': asignacion.materia.dias_semana,
                    'descripcion': asignacion.materia.descripcion,

                    'curso': 
                    {
                        'nombre': asignacion.materia.curso.nombre
                    },


                    'aula': 
                    {
                        'nombre': asignacion.materia.aula.nombre
                    },

                    'especialidad': 
                    (
                         {'nombre': asignacion.materia.especialidades.first().nombre}
                         if asignacion.materia.especialidades.exists()
                         else {'nombre': 'Sin especialidad'}
                    ),

                },

                'grupo': 
                {
                    'nombre': asignacion.grupo.nombre
                },

                'situacion_revista': asignacion.situacion_revista

            })
        
        return JsonResponse(data, safe=False)
    
class DocenteCreateView(CreateView):
    model = Docente
    form_class = DocenteForm
    template_name = 'alta_docente.html'
    success_url = reverse_lazy('docentes_listado')
    
    def form_valid(self, form):
        return super().form_valid(form)

class DocenteDetailView(DetailView):
    model = Docente
    template_name = 'docente_detalle.html'
    context_object_name = 'docente'


# ESPECIALIDADES

class EspecialidadCreateView(SuccessMessageMixin, CreateView):
    model = Especialidad
    form_class = EspecialidadForm
    template_name = 'crear_especialidades.html'
    success_url = reverse_lazy('gestion_especialidades')
    success_message = "Especialidad creada exitosamente."

class EspecialidadListView(ListView):
    model = Especialidad
    template_name = 'gestion_especialidades.html'
    context_object_name = 'especialidades'    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Gestión de Especialidades'
        return context

class EspecialidadDeleteView(DeleteView):
    model = Especialidad
    template_name = 'eliminar_especialidad.html' 
    success_url = reverse_lazy('gestion_especialidades')

    def get_object(self, queryset=None):
        return Especialidad.objects.get(nombre=self.kwargs['nombre'])

class EspecialidadUpdateView(UpdateView):
    model = Especialidad
    form_class = EspecialidadForm
    template_name = 'editar_especialidad.html'
    success_url = reverse_lazy('gestion_especialidades')

# TURNOS

class TurnoCreateView(SuccessMessageMixin, CreateView):
    model = Turno
    form_class = TurnoForm
    template_name = 'crear_turnos.html'
    success_url = reverse_lazy('gestion_turnos')
    success_message = "Turno creado exitosamente."

class TurnoListView(ListView):
    
    model = Turno
    template_name = 'gestion_turnos.html'
    context_object_name = 'object_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["nombres_distintos"] = Turno.objects.values_list("nombre", flat=True).distinct()
        context["horas_inicio_distintas"] = Turno.objects.values_list("hora_inicio", flat=True).distinct()
        return context

class TurnoDeleteView(DeleteView):
    model = Turno
    template_name = 'eliminar_turno.html' 
    success_url = reverse_lazy('gestion_turnos')

    def get_object(self, queryset=None):
        return Turno.objects.get(nombre=self.kwargs['nombre'])

class TurnoUpdateView(UpdateView):
    model = Turno
    form_class = TurnoForm
    template_name = 'editar_turno.html'
    success_url = reverse_lazy('gestion_turnos')

# CURSOS

class CursoCreateView(SuccessMessageMixin, CreateView):
    model = Curso
    form_class = CursoForm
    template_name = 'crear_cursos.html'
    success_url = reverse_lazy('gestion_cursos')  
    success_message = "Curso creado exitosamente."

class CursoListView(ListView):
    model = Curso
    template_name = 'gestion_cursos.html'
    context_object_name = 'cursos'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cursos'] = Curso.objects.all()
        context['especialidades'] = Especialidad.objects.all()
        context['titulo'] = 'Gestión de Cursos'
        return context
    
class CursoDeleteView(DeleteView):
    model = Curso
    template_name = 'eliminar_curso.html' 
    success_url = reverse_lazy('gestion_cursos')

    def get_object(self, queryset=None):
        return Curso.objects.get(nombre=self.kwargs['nombre'])

class CursoUpdateView(UpdateView):
    model = Curso
    form_class = CursoForm
    template_name = 'editar_curso.html'
    success_url = reverse_lazy('gestion_cursos')

# GRUPOS

class GrupoCreateView(SuccessMessageMixin, CreateView):
    model = Grupo
    form_class = GrupoForm
    template_name = 'crear_grupos.html'
    success_url = reverse_lazy('gestion_grupos')
    success_message = "Grupo creado exitosamente."

class GrupoListView(ListView):
    model = Grupo
    template_name = 'gestion_grupos.html'
    context_object_name = 'grupos'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Gestión de Grupos'
        return context

class GrupoDeleteView(DeleteView):
    model = Grupo
    template_name = 'eliminar_grupo.html' 
    success_url = reverse_lazy('gestion_grupos')

    def get_object(self, queryset=None):
        return Grupo.objects.get(nombre=self.kwargs['nombre'])

class GrupoUpdateView(UpdateView):
    model = Grupo
    form_class = GrupoForm
    template_name = 'editar_grupo.html'
    success_url = reverse_lazy('gestion_grupos')

# IMPORT / EXPORT

class ImportarAlumnosView(View):
    template_name = 'importar_alumnos.html'
    #success_url = 'importar_alumnos_exito'

    def get(self, request):
        form = AlumnoUploadFileForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = AlumnoUploadFileForm(request.POST, request.FILES)

        if not form.is_valid():
            return render(request, self.template_name, {'form': form})

        archivo_excel = form.cleaned_data['file']

        try:
            wb = load_workbook(filename=archivo_excel)
            hoja = wb.active

            for i, fila in enumerate(hoja.iter_rows(min_row=2, values_only=True), start=2):
                try:
                    nombre, apellido, dni, cuil, fecha_nacimiento, libro, folio, numero_legajo, libro_matriz, folio_matriz, email, telefono, domicilio, curso_id, especialidad_id, grupo_id = fila
                    
                    # Manejo de fecha_nacimiento
                    fecha_nac = None
                    if fecha_nacimiento:
                        if isinstance(fecha_nacimiento, datetime):
                            fecha_nac = fecha_nacimiento.date()
                        elif isinstance(fecha_nacimiento, str):
                            fecha_nac = datetime.strptime(fecha_nacimiento, "%Y-%m-%d").date()
                        else:
                            fecha_nac = datetime(2000, 1, 1).date()  # Valor por defecto
                    
                    alumno = Alumno(
                        nombre=nombre,
                        apellido=apellido,
                        dni=int(dni),
                        cuil=str(cuil),
                        fecha_nacimiento=fecha_nac if fecha_nac else datetime(2000, 1, 1).date(),  # Valor por defecto
                        libro=libro or "",
                        folio=folio or "",
                        numero_legajo=numero_legajo or "",
                        libro_matriz=libro_matriz or "",
                        folio_matriz=folio_matriz or "",
                        email=email or "",
                        telefono=telefono or "",
                        domicilio=domicilio or "",
                        curso=Curso.objects.get(id=curso_id) if curso_id else None,
                        especialidad=Especialidad.objects.get(id=especialidad_id) if especialidad_id else None,
                        grupo=Grupo.objects.get(id=grupo_id) if grupo_id else None,
                    )

                    alumno.full_clean()
                    alumno.save()

                except ValidationError as ve:
                    messages.warning(request, f"Error en la fila {i}: {ve}")
                except Exception as e:
                    messages.warning(request, f"Error procesando la fila {i}: {str(e)}")

            messages.success(request, "Importación completada.")

        except Exception as e:
            messages.error(request, f"Error leyendo el archivo: {e}")

        return redirect('importar_alumnos_exito')
        
class ImportarAlumnosExitoView(TemplateView):
    template_name = 'importar_alumnos_exito.html'
    
    def get(self, request, *args, **kwargs):
        # Asegúrate que solo se acceda por GET
        if 'import_result' not in request.session:
            return redirect('importar_alumnos')
        return super().get(request, *args, **kwargs)
    
# MATERIA

class CrearMateriaYGrupoView(View):
    template_name = 'crear_materia_grupo.html'

    def get(self, request):
        materia_form = MateriaForm()
        grupo_materia_form = GrupoMateriaForm()
        return render(request, self.template_name, {
            'materia_form': materia_form,
            'grupo_materia_form': grupo_materia_form,
        })

    def post(self, request):
        materia_form = MateriaForm(request.POST)
        grupo_materia_form = GrupoMateriaForm(request.POST)

        if materia_form.is_valid() and grupo_materia_form.is_valid():
            materia_nombre = materia_form.cleaned_data['nombre']
            materia_curso = materia_form.cleaned_data['curso']
            grupo = grupo_materia_form.cleaned_data['grupo']
            especialidades = materia_form.cleaned_data['especialidades']

            # Buscar si ya existe una materia con ese nombre, curso, grupo y especialidad
            materias_existentes = GrupoMateria.objects.filter(
                materia__nombre=materia_nombre,
                materia__curso=materia_curso,
                grupo=grupo
            )

            for gm in materias_existentes:
                if set(gm.materia.especialidades.all()) == set(especialidades):
                    messages.error(request, "❌ Ya existe una asignación con esta combinación de materia, curso, grupo y especialidad.")
                    return render(request, self.template_name, {
                        'materia_form': materia_form,
                        'grupo_materia_form': grupo_materia_form,
                    })

            # Guardar la materia y la relación
            materia = materia_form.save()
            grupo_materia = grupo_materia_form.save(commit=False)
            grupo_materia.materia = materia
            grupo_materia.save()
            grupo_materia_form.save_m2m()  # Por si hubiera campos many-to-many en el form

            messages.success(request, "✅ Materia y asignación creadas correctamente.")
            return redirect('materias_listado')  # Reemplazá con la URL correcta

        return render(request, self.template_name, {
            'materia_form': materia_form,
            'grupo_materia_form': grupo_materia_form,
        })
    
class ListaMateriasView(ListView):

    model = Materia
    template_name = 'materias_listado.html'
    context_object_name = 'materias'

    def get_queryset(self):
        return Materia.objects.select_related('aula', 'curso').prefetch_related(
            'especialidades',
            Prefetch(
                'grupo_asignaciones',
                queryset=GrupoMateria.objects.select_related('grupo', 'docente')
            )
        )
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Agregar listas para filtros
        context['cursos'] = Curso.objects.all().order_by('nombre')
        context['grupos'] = Grupo.objects.all().order_by('nombre')
        context['especialidades'] = Especialidad.objects.all().order_by('nombre')

        return context

class EditarMateriaYGrupoView(View):
    template_name = 'editar_materia_grupo.html'

    def get(self, request, pk):
        # pk es el id de GrupoMateria a editar (podría ser materia si preferís)
        grupo_materia = get_object_or_404(GrupoMateria, pk=pk)
        materia = grupo_materia.materia

        materia_form = MateriaForm(instance=materia)
        grupo_materia_form = GrupoMateriaForm(instance=grupo_materia)

        return render(request, self.template_name, {
            'materia_form': materia_form,
            'grupo_materia_form': grupo_materia_form,
            'grupo_materia': grupo_materia,
        })

    def post(self, request, pk):
        grupo_materia = get_object_or_404(GrupoMateria, pk=pk)
        materia = grupo_materia.materia

        materia_form = MateriaForm(request.POST, instance=materia)
        grupo_materia_form = GrupoMateriaForm(request.POST, instance=grupo_materia)

        if materia_form.is_valid() and grupo_materia_form.is_valid():
            materia = materia_form.save()
            grupo_materia = grupo_materia_form.save(commit=False)
            grupo_materia.materia = materia
            grupo_materia.save()
            grupo_materia_form.save_m2m()

            messages.success(request, "✅ Materia y asignación actualizadas correctamente.")
            return redirect('materias_listado')

        return render(request, self.template_name, {
            'materia_form': materia_form,
            'grupo_materia_form': grupo_materia_form,
            'grupo_materia': grupo_materia,
        })

class EliminarMateriaYGrupoView(View):

    template_name = 'eliminar_materia_grupo_confirmacion.html'

    def get(self, request, pk):
        grupo_materia = get_object_or_404(GrupoMateria, pk=pk)
        especialidades = grupo_materia.materia.especialidades.all()

        return render(request, self.template_name, {
            'grupo_materia': grupo_materia,
            'especialidades': especialidades,
        })

    def post(self, request, pk):
        grupo_materia = get_object_or_404(GrupoMateria, pk=pk)
        materia = grupo_materia.materia

        grupo_materia.delete()

        if materia.grupo_asignaciones.count() == 0:
            materia.delete()
            messages.success(request, "🗑️ Materia y asignación eliminadas correctamente.")
        else:
            messages.warning(request, "⚠️ Asignación eliminada, pero la materia sigue asociada a otros grupos.")

        return redirect('materias_listado')

#TIPO CARGOS

class GestionCargosView(TemplateView):
    template_name = 'gestion_cargos.html'

class TipoCargoListView(ListView):
    model = TipoCargo
    template_name = 'tipocargo_listado.html'
    context_object_name = 'tipo_cargo'

class TipoCargoUpdateView(UpdateView):
    model = TipoCargo
    fields = ['nombre', 'descripcion']
    template_name = 'editar_tipocargo.html'
    success_url = reverse_lazy('cargos_listado')

class TipoCargoDeleteView(DeleteView):
    model = TipoCargo
    template_name = 'eliminar_tipocargo_confirmacion.html'
    success_url = reverse_lazy('cargos_listado')

class TipoCargoCreateView(CreateView):

    model = TipoCargo
    fields = ['nombre', 'descripcion']
    template_name = 'crear_tipocargo.html'
    success_url = reverse_lazy('cargos_listado')

#ASIGNACION CARGOS

class CargoListView(ListView):
    model = Cargo
    template_name = 'asgcargos_listado.html'
    context_object_name = 'cargos'

    def get_queryset(self):
    
        qs = super().get_queryset()
        return qs.select_related('docente', 'cargo').prefetch_related('curso')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Listado de Cargos"
        
        context['cargos_unicos'] = (
            self.get_queryset()
            .values_list('cargo__nombre', flat=True)
            .distinct()
            .order_by('cargo__nombre')
        )
        return context

class CargoCreateView(CreateView):

    model = Cargo
    form_class = CargoForm
    template_name = 'crear_cargo.html'
    success_url = reverse_lazy('asgcargos_listado')

class CargoDetailView(DetailView):

    model = Cargo
    template_name = 'detcargo_listado.html'
    context_object_name = 'cargo'
    success_url = reverse_lazy('asgcargos_listado')

class CargoUpdateView(UpdateView):
    model = Cargo
    form_class = CargoForm
    template_name = 'editcargo_listado.html'
    success_url = reverse_lazy('cargos_listado')

class CargoDeleteView(DeleteView):
    model = Cargo
    template_name = 'eliminar_cargo_confirmacion.html'
    success_url = reverse_lazy('asgcargos_listado')



