from django.contrib import admin
from .models import Asistencia, Turno, TipoAsistencia

#///////////////////////////////////////////////

@admin.register(Asistencia)
class AsistenciaAdmin(admin.ModelAdmin):
    list_display = ('alumno', 'fecha', 'tipo', 'estado')            # columnas en la lista
    list_filter = ('fecha', 'tipo', 'estado')                       # filtros laterales
    search_fields = ('alumno__nombre', 'alumno__apellido')          # búsqueda por nombre/apellido
    date_hierarchy = 'fecha'                                        # navegación por fecha
    ordering = ('-fecha', 'alumno')                                 # orden predeterminado

@admin.register(TipoAsistencia)
class TipoAsistenciaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
