# alumnos/urls.py
from django.urls import path # type: ignore
from .views import Alumnos_listado_view, AlumnoDeleteView, AlumnoUpdateView, AlumnoCreateView, AlumnoDatosView, AlumnoDatosCUILView
from .views import ImportarAlumnosView, ImportarAlumnosExitoView
from .views import Docentes_listado_view, DocenteMateriasView, DocenteDeleteView, DocenteCreateView, DocenteUpdateView, DocenteDetailView
from .views import EspecialidadListView
from .views import GrupoListView, GrupoCreateView, GrupoDeleteView, GrupoUpdateView
from .views import TurnoListView, TurnoCreateView, TurnoDeleteView, TurnoUpdateView
from .views import CursoListView, CursoCreateView, CursoDeleteView, CursoUpdateView
from .views import EspecialidadCreateView,EspecialidadDeleteView, EspecialidadUpdateView
from .views import CrearMateriaYGrupoView, ListaMateriasView, EditarMateriaYGrupoView, EliminarMateriaYGrupoView
from .views import GestionCargosView, TipoCargoListView,TipoCargoUpdateView, TipoCargoDeleteView, TipoCargoCreateView
from .views import CargoListView, CargoCreateView, CargoDetailView, CargoUpdateView, CargoDeleteView

urlpatterns = [

    path('', Alumnos_listado_view.as_view(), name='alumnos_listado'),
    path('editar/<str:cuil>/', AlumnoUpdateView.as_view(), name='editar_alumno'),
    path('eliminar/<str:cuil>/', AlumnoDeleteView.as_view(), name='eliminar_alumno'),
    path('nuevo/', AlumnoCreateView.as_view(), name='alta_alumno'),

    path('importar-alumnos/', ImportarAlumnosView.as_view(), name='importar_alumnos'),
    path('importar-alumnos-exito/', ImportarAlumnosExitoView.as_view(), name='importar_alumnos_exito'),

    path("datos-alumno/", AlumnoDatosView.as_view(), name="datos_alumno"),
    path('datos-alumno/<str:cuil>/', AlumnoDatosCUILView.as_view(), name='editar_datos_alumno'),

    path('docentes/', Docentes_listado_view.as_view(), name='docentes_listado'),
    path('docentes/<int:pk>/materias/', DocenteMateriasView.as_view(), name='docente_materia'),
    path('docentes/eliminar/<str:cuil>', DocenteDeleteView.as_view(), name='eliminar_docente' ),
    path('docentes/nuevo/', DocenteCreateView.as_view(), name='alta_docente'),
    path('docentes/editar/<str:cuil>/', DocenteUpdateView.as_view(), name='editar_docente'),
    path('docente/<int:pk>/', DocenteDetailView.as_view(), name='docente_detail'),


    path('especialidades/nueva', EspecialidadCreateView.as_view(), name='crear_especialidades'),     
    path('especialidades/gestion', EspecialidadListView.as_view(), name='gestion_especialidades'),
    path('especialidades/eliminar/<str:nombre>', EspecialidadDeleteView.as_view(), name='eliminar_especialidad' ),
    path('especialidades/editar/<int:pk>/', EspecialidadUpdateView.as_view(), name='especialidad_editar'),
    
    path('turno/gestion', TurnoListView.as_view(), name='gestion_turnos'),
    path('turno/nuevo', TurnoCreateView.as_view(), name='crear_turnos'),
    path('turno/eliminar/<str:nombre>', TurnoDeleteView.as_view(), name='eliminar_turno' ),
    path('turno/editar/<int:pk>/', TurnoUpdateView.as_view(), name='turno_editar'),
    
    
    path('curso/nuevo', CursoCreateView.as_view(), name='crear_cursos'),
    path('curso/gestion', CursoListView.as_view(), name='gestion_cursos'),
    path('curso/eliminar/<str:nombre>', CursoDeleteView.as_view(), name='eliminar_curso' ),
    path('curso/editar/<int:pk>/', CursoUpdateView.as_view(), name='curso_editar'),

    path('grupo/gestion', GrupoListView.as_view(), name='gestion_grupos'),
    path('grupo/nuevo', GrupoCreateView.as_view(), name='crear_grupos'),
    path('grupo/eliminar/<str:nombre>', GrupoDeleteView.as_view(), name='eliminar_grupo' ),
    path('grupo/editar/<int:pk>/', GrupoUpdateView.as_view(), name='grupo_editar'),

    path('materia/', ListaMateriasView.as_view(), name='materias_listado'),
    path('materia/nueva/', CrearMateriaYGrupoView.as_view(), name='crear_materia_grupo'),
    path('materia/editar/<int:pk>/', EditarMateriaYGrupoView.as_view(), name='materia_editar'),
    path('materia/eliminar/<int:pk>', EliminarMateriaYGrupoView.as_view(), name='eliminar_materia' ),


    path('gcargos/', GestionCargosView.as_view(), name='gestion_cargos'),
    path('cargos/', TipoCargoListView.as_view(), name='cargos_listado'),
    path('cargo/editar/<int:pk>/', TipoCargoUpdateView.as_view(), name='tipocargo_editar'),
    path('cargo/eliminar/<int:pk>', TipoCargoDeleteView.as_view(), name='tipocargo_eliminar' ),
    path('cargo/nuevo', TipoCargoCreateView.as_view(), name='crear_cargo'), 

    path('asgcargos/', CargoListView.as_view(), name='asgcargos_listado'),
    path('asgcargo/nuevo', CargoCreateView.as_view(), name='crear_asgcargo'),
    path('asgcargos/<int:pk>/', CargoDetailView.as_view(), name='detcargo_listado'),
    path('asgcargo/editar/<int:pk>/', CargoUpdateView.as_view(), name='asgcargo_editar'),
    path('asgcargo/eliminar/<int:pk>', CargoDeleteView.as_view(), name='cargo_eliminar' ),


]