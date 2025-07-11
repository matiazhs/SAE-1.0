
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django.contrib import admin
from .models import Aula, Grupo, Especialidad, Turno, Curso, Materia, Docente, GrupoMateria, Alumno, TipoCargo, Cargo

@admin.register(Aula)
class AulaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo', 'capacidad')
    search_fields = ('nombre',)
    list_filter = ('tipo',)

@admin.register(Grupo)
class GrupoAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

@admin.register(Especialidad)
class EspecialidadAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

@admin.register(Turno)
class TurnoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'hora_inicio', 'hora_fin')
    search_fields = ('nombre',)

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

@admin.register(Materia)
class MateriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo', 'curso', 'aula')
    search_fields = ('nombre', 'curso__nombre')
    list_filter = ('tipo', 'curso')

@admin.register(Docente)
class DocenteAdmin(admin.ModelAdmin):
    list_display = ('apellido', 'nombre', 'cuil', 'numero_legajo')
    search_fields = ('apellido', 'nombre', 'cuil', 'numero_legajo')

@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
    list_display = ('id','apellido', 'nombre', 'dni', 'curso', 'grupo', 'especialidad', 'activo')
    search_fields = ('apellido', 'nombre', 'dni', 'numero_legajo')
    list_filter = ('activo', 'curso', 'grupo', 'especialidad')


@admin.register(TipoCargo)
class TipoCargoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')  # columnas visibles en el listado
    search_fields = ('nombre',)              # habilita búsqueda por nombre
    list_per_page = 20                       # cantidad de ítems por página

@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = (
        'get_apellido', 'get_nombre', 'get_cuil', 'get_domicilio', 'get_fecha_nacimiento',
        'get_email', 'get_numero_legajo', 'get_telefono', 'get_telefono_emergencia',
        'get_fecha_ingreso', 'cargo', 'especialidades',
    )

    search_fields = (
        'docente__apellido', 'docente__nombre', 'docente__cuil', 'docente__numero_legajo',
        'docente__email', 'docente__telefono', 'docente__telefono_emergencia'
    )

    list_filter = (
        'cargo', 'especialidades', 'curso',
    )

    filter_horizontal = ('curso',)
    ordering = ('docente__apellido', 'docente__nombre')
    date_hierarchy = None  # No se puede usar con campos relacionados directamente

    fieldsets = (
        ('Datos personales del Docente', {
            'fields': (
                'docente',
            )
        }),
        ('Datos del Cargo', {
            'fields': (
                'cargo',
                'especialidades',
                'curso',
            )
        }),
    )

    # Métodos para acceder a los datos del docente
    def get_apellido(self, obj):
        return obj.docente.apellido if obj.docente else '-'
    get_apellido.short_description = 'Apellido'
    get_apellido.admin_order_field = 'docente__apellido'

    def get_nombre(self, obj):
        return obj.docente.nombre if obj.docente else '-'
    get_nombre.short_description = 'Nombre'
    get_nombre.admin_order_field = 'docente__nombre'

    def get_cuil(self, obj):
        return obj.docente.cuil if obj.docente else '-'

    def get_domicilio(self, obj):
        return obj.docente.domicilio if obj.docente else '-'

    def get_fecha_nacimiento(self, obj):
        return obj.docente.fecha_nacimiento if obj.docente else '-'

    def get_email(self, obj):
        return obj.docente.email if obj.docente else '-'

    def get_numero_legajo(self, obj):
        return obj.docente.numero_legajo if obj.docente else '-'

    def get_telefono(self, obj):
        return obj.docente.telefono if obj.docente else '-'

    def get_telefono_emergencia(self, obj):
        return obj.docente.telefono_emergencia if obj.docente else '-'

    def get_fecha_ingreso(self, obj):
        return obj.docente.fecha_ingreso if obj.docente else '-'

#///////////////////////////////////////////////

class GrupoMateriaForm(ModelForm):
    def clean(self):
        cleaned_data = super().clean()
        if 'materia' in cleaned_data and 'grupo' in cleaned_data:
            materia = cleaned_data['materia']
            grupo = cleaned_data['grupo']

            if GrupoMateria.objects.exclude(pk=self.instance.pk).filter(
                grupo=grupo,
                materia__nombre=materia.nombre,
                materia__curso=materia.curso
            ).exists():
                raise ValidationError("Ya existe una asignación con el mismo nombre de materia, curso y grupo.")

        return cleaned_data

class GrupoMateriaAdmin(admin.ModelAdmin):
    form = GrupoMateriaForm

admin.site.register(GrupoMateria, GrupoMateriaAdmin)