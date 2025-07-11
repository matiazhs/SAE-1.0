from django.db import models # type: ignore
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator # type: ignore



class AlumnoDatos(models.Model):

    SI_NO_CHOICES = [
        ('si', 'Sí'),
        ('no', 'No'),
    ]

    # DATOS ESTUDIANTE
    apellido = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField(null=True)

    posee_dni = models.CharField(max_length=20, blank=True)
    cpi = models.CharField(max_length=2, choices=SI_NO_CHOICES, blank=True)
    doc_extranjero = models.CharField(max_length=2, choices=SI_NO_CHOICES, blank=True)
    tipo_doc_extranjero = models.CharField(max_length=50, blank=True)
    num_doc_extranjero = models.CharField(max_length=50, blank=True)
    num_dni = models.CharField(max_length=20, blank=True)
    cuil = models.CharField(max_length=20, blank=True)

    identidad_genero = models.CharField(max_length=20, blank=True)
    identidad_genero_otra = models.CharField(max_length=100, blank=True)

    lugar_nacimiento = models.CharField(max_length=20)
    nacionalidad = models.CharField(max_length=100, blank=True)
    nac_argentina_opcion = models.CharField(max_length=20, blank=True)
    provincia = models.CharField(max_length=100, blank=True)

    distrito = models.CharField(max_length=100, blank=True)
    localidad = models.CharField(max_length=100, blank=True)
    calle = models.CharField(max_length=100, blank=True)
    numero = models.CharField(max_length=10, blank=True)
    piso = models.CharField(max_length=10, blank=True)
    torre = models.CharField(max_length=10, blank=True)
    departamento = models.CharField(max_length=10, blank=True)
    entre_calle = models.CharField(max_length=100, blank=True)
    y_calle = models.CharField(max_length=100, blank=True)
    otro_dato = models.CharField(max_length=100, blank=True)
    telefono = models.CharField(max_length=20, blank=True)
    telefono_celular = models.CharField(max_length=20, blank=True)

    tiene_hermanos = models.CharField(max_length=2, choices=SI_NO_CHOICES, blank=True)
    cantidad_hermanos = models.IntegerField(null=True, blank=True)
    hermanos_en_institucion = models.IntegerField(null=True, blank=True)

    idioma_hogar = models.CharField(max_length=2, choices=SI_NO_CHOICES, blank=True)
    leng_indigenas = models.CharField(max_length=2, choices=SI_NO_CHOICES, blank=True)
    otras_leng = models.CharField(max_length=2, choices=SI_NO_CHOICES, blank=True)

    des_porg = models.CharField(max_length=2, choices=SI_NO_CHOICES, blank=True)
    per_auh = models.CharField(max_length=2, choices=SI_NO_CHOICES, blank=True)
    per_prog = models.CharField(max_length=2, choices=SI_NO_CHOICES, blank=True)

    medio_transporte = models.JSONField(blank=True, null=True)  # Puede almacenar lista de medios seleccionados

    tiene_hijos = models.CharField(max_length=2, choices=SI_NO_CHOICES, blank=True)
    asiste_maternales = models.CharField(max_length=2, choices=SI_NO_CHOICES, blank=True)

    # INFORMACION SALUD

    obra_social = models.CharField(max_length=2, choices=SI_NO_CHOICES, blank=True)
    obrsoc = models.CharField(max_length=20, blank=True)
    n_afil = models.CharField(max_length=20, blank=True)

    info_salud_izq = models.JSONField(blank=True, null=True)
    info_salud_der = models.JSONField(blank=True, null=True)

    ejercicio_izq = models.JSONField(blank=True, null=True)

    ejercicio_der = models.JSONField(blank=True, null=True)

    int_comun = models.CharField(max_length=2, choices=SI_NO_CHOICES, blank=True)
    cuantas_veces = models.CharField(max_length=20, blank=True)
    causas_diag = models.CharField(max_length=20, blank=True)

    int_int = models.CharField(max_length=2, choices=SI_NO_CHOICES, blank=True)
    cuantas_veces_2 = models.CharField(max_length=20, blank=True)
    causas_diag_2 = models.CharField(max_length=20, blank=True)

    aler_graves = models.CharField(max_length=2, choices=SI_NO_CHOICES, blank=True)
    alergias_izq = models.JSONField(blank=True, null=True)
    alergias_der = models.JSONField(blank=True, null=True)
    medicamentos_confirma = models.CharField(max_length=2, choices=SI_NO_CHOICES, blank=True)
    vacunas_confirma = models.CharField(max_length=2, choices=SI_NO_CHOICES, blank=True)
    alimentos_confirma = models.CharField(max_length=2, choices=SI_NO_CHOICES, blank=True)
    picaduras_confirma = models.CharField(max_length=2, choices=SI_NO_CHOICES, blank=True)
    estacionales_confirma = models.CharField(max_length=2, choices=SI_NO_CHOICES, blank=True)
    otras_confirma = models.CharField(max_length=2, choices=SI_NO_CHOICES, blank=True)

    dis_auditiva = models.CharField(max_length=2, choices=SI_NO_CHOICES, blank=True)
    usa_audifono = models.CharField(max_length=2, choices=SI_NO_CHOICES, blank=True)
    dis_visual = models.CharField(max_length=2, choices=SI_NO_CHOICES, blank=True)
    usa_lentes = models.CharField(max_length=2, choices=SI_NO_CHOICES, blank=True)

    recive_med = models.CharField(max_length=2, choices=SI_NO_CHOICES, blank=True)
    cual_med = models.CharField(max_length=100, blank=True)

    alg_op = models.CharField(max_length=2, choices=SI_NO_CHOICES, blank=True)
    xq_motivo = models.CharField(max_length=100, blank=True)
    en_que_year = models.CharField(max_length=20, blank=True)

    ant_salud_izq = models.JSONField(blank=True, null=True)
    ant_salud_der = models.JSONField(blank=True, null=True)

    # DATOS DEL ESTABLECIMIENTO

    sector_pp = models.CharField(max_length=10, choices=[("privado", "Privado"), ("publico", "Publico")], blank=True)

    distrito_esta = models.CharField(max_length=100, blank=True)
    nom_escuela = models.CharField(max_length=100, blank=True)
    numero_esta = models.CharField(max_length=100, blank=True)
    cue = models.CharField(max_length=100, blank=True)
    clave_prov = models.CharField(max_length=100, blank=True)


    distrito_proc = models.CharField(max_length=100, blank=True)
    nom_escuela_proc = models.CharField(max_length=100, blank=True)
    numero_proc = models.CharField(max_length=20, blank=True)
    nivel_mod = models.CharField(max_length=100, blank=True)
    sector_pp_3 = models.CharField(max_length=10, choices=[("privado", "Privado"), ("publico", "Publico")], blank=True)
    dependencias = models.JSONField(blank=True, null=True)

    select_prov = models.CharField(max_length=10, blank=True)
    prov_4 = models.CharField(max_length=100, blank=True)

    # DATOS DEL INSCRIPCION

    cursa_p_inclu = models.CharField(max_length=20, blank=True)
    esc_cursa = models.CharField(max_length=20, blank=True)
    tiene_acomp = models.CharField(max_length=20, blank=True)

    # EDUCACION COMPLEMENTARIA

    ins_en = models.CharField(max_length=20, blank=True)
    orient = models.CharField(max_length=20, blank=True)
    anoo = models.CharField(max_length=20, blank=True)
    tur = models.CharField(max_length=20, blank=True)
    jornadas = models.CharField(max_length=20, blank=True)
    ins_act = models.CharField(max_length=20, blank=True)


    asis_inst = models.CharField(max_length=20, blank=True)
    asis_inst_2 = models.CharField(max_length=20, blank=True)
    asis_inst_3 = models.CharField(max_length=20, blank=True)
    incorp_serv_esc = models.JSONField(blank=True, null=True)

    # ADULTOS RESPONSABLES

    vinc_est = models.JSONField(blank=True, null=True)
    vinc_est2 = models.JSONField(blank=True, null=True)

    ape_adul_1 = models.CharField(max_length=100, blank=True)
    nombre_adul_1 = models.CharField(max_length=100, blank=True)
    nac_adul_1 = models.CharField(max_length=100, blank=True)

    ape_adul_2 = models.CharField(max_length=100, blank=True)
    nombre_adul_2 = models.CharField(max_length=100, blank=True)
    nac_adul_2 = models.CharField(max_length=100, blank=True)

    dni_adul_1 = models.CharField(max_length=20, blank=True)
    dni_adul_2 = models.CharField(max_length=20, blank=True)
    ndoc_adul_1 = models.CharField(max_length=100, blank=True)
    ndoc_adul_2 = models.CharField(max_length=100, blank=True)
    po_cdi = models.CharField(max_length=20, blank=True)
    po_cdi2 = models.CharField(max_length=20, blank=True)

    doc_extra1 = models.CharField(max_length=20, blank=True)
    doc_extra2 = models.CharField(max_length=20, blank=True)
    ndoc_adul_extra_1 = models.CharField(max_length=100, blank=True)
    ndoc_adul_extra_2 = models.CharField(max_length=100, blank=True)

    prof_edu_1 = models.CharField(max_length=100, blank=True)
    prof_edu_2 = models.CharField(max_length=100, blank=True)
    asis_esta_edu_adul_1 = models.CharField(max_length=20, blank=True)
    asis_esta_edu_adul_2 = models.CharField(max_length=20, blank=True)
    niv_curso_1 = models.CharField(max_length=100, blank=True)
    niv_curso_2 = models.CharField(max_length=100, blank=True)
    comp_niv_1 = models.CharField(max_length=20, blank=True)
    comp_niv_2 = models.CharField(max_length=20, blank=True)

    con_act_1 = models.CharField(max_length=20, blank=True)
    con_act_2 = models.CharField(max_length=20, blank=True)

    vive_est_1 = models.CharField(max_length=20, blank=True)
    vive_est_2 = models.CharField(max_length=20, blank=True)

    calle_f_1 = models.CharField(max_length=100, blank=True)
    numero_f_1 = models.CharField(max_length=100, blank=True)
    piso_f_1 = models.CharField(max_length=100, blank=True)
    torre_f_1 = models.CharField(max_length=100, blank=True)
    departamento_f_1 = models.CharField(max_length=100, blank=True)
    entre_calle_f_1 = models.CharField(max_length=100, blank=True)
    y_calle_f_1 = models.CharField(max_length=100, blank=True)
    otro_dato_f_1 = models.CharField(max_length=100, blank=True)
    provincia_f_1 = models.CharField(max_length=100, blank=True)
    distrito_f_1 = models.CharField(max_length=100, blank=True)
    localidad_f_1 = models.CharField(max_length=100, blank=True)
    telefono_f_1 = models.CharField(max_length=100, blank=True)
    telefono_celular_f_1 = models.CharField(max_length=100, blank=True)
    email_f_1 = models.CharField(max_length=100, blank=True)

    calle_f_2 = models.CharField(max_length=100, blank=True)
    numero_f_2 = models.CharField(max_length=100, blank=True)
    piso_f_2 = models.CharField(max_length=100, blank=True)
    torre_f_2 = models.CharField(max_length=100, blank=True)
    departamento_f_2 = models.CharField(max_length=100, blank=True)
    entre_calle_f_2 = models.CharField(max_length=100, blank=True)
    y_calle_f_2 = models.CharField(max_length=100, blank=True)
    otro_dato_f_2 = models.CharField(max_length=100, blank=True)
    provincia_f_2 = models.CharField(max_length=100, blank=True)
    distrito_f_2 = models.CharField(max_length=100, blank=True)
    localidad_f_2 = models.CharField(max_length=100, blank=True)
    telefono_f_2 = models.CharField(max_length=100, blank=True)
    telefono_celular_f_2 = models.CharField(max_length=100, blank=True)
    email_f_2 = models.CharField(max_length=100, blank=True)

    ape_f = models.CharField(max_length=100, blank=True)
    nomb_f = models.CharField(max_length=100, blank=True)
    tipo_f = models.CharField(max_length=100, blank=True)
    num_f = models.CharField(max_length=100, blank=True)
    des_f = models.CharField(max_length=400, blank=True)
    

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"

#region [Documentación Grupo]
"""
Representa un grupo de alumnos (como 'A', 'B') dentro de un curso.
Atributos:
  nombre: Nombre identificatorio único del grupo
  descripcion: Información adicional opcional
Relaciones:
  alumnos: Alumnos asignados a este grupo
  materia_asignaciones: Materias asignadas a este grupo
"""
#endregion
class Grupo(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

#region [Documentación Especialidad]
"""
Área de especialización académica ofrecida.
Atributos:
  nombre: Nombre de la especialidad
  descripcion: Descripción del programa
Relaciones:
  cursos: Cursos que incluyen esta especialidad
  materias: Materias de esta especialidad
  alumnos: Alumnos inscriptos
"""
#endregion
class Especialidad(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

#region [Documentación Turno]
"""
Franja horaria para clases (mañana/tarde/noche).
Atributos:
  nombre: Nombre del turno
  hora_inicio: Comienzo del turno
  hora_fin: Finalización del turno
  descripcion: Detalles adicionales
Relaciones:
  cursos: Cursos en este turno
"""
#endregion
class Turno(models.Model):
    nombre = models.CharField(max_length=50)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return f"{self.nombre} ({self.hora_inicio.strftime('%H:%M')}-{self.hora_fin.strftime('%H:%M')})"

#region [Documentación Curso]
"""
Nivel académico que agrupa alumnos por año.
Atributos:
  nombre: Nombre del curso
  año: Año académico (1-10)
  activo: Indica si está activo
Relaciones:
  especialidades: Especialidades asociadas
  turnos: Turnos disponibles
  materias: Materias del curso
  alumnos: Alumnos inscriptos
"""
#endregion
class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    año = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    activo = models.BooleanField(default=True)

    especialidades = models.ManyToManyField(Especialidad, related_name='cursos')
    turnos = models.ManyToManyField(Turno, related_name='cursos')

    def __str__(self):
        return f"{self.nombre} - Año {self.año}"

#region [Documentación Materia]
"""
Asignatura o disciplina que se enseña.
Atributos:
  nombre: Nombre de la materia
  tipo: Taller/Teoría
  pid: Identificador plan de estudios
  cupof: Cupo femenino
  ftp: Fecha toma de posesión
  foin: Forma de ingreso
  horario: Horas semanales
  descripcion: Detalles adicionales
Relaciones:
  curso: Curso al que pertenece
  especialidades: Especialidades que la incluyen
  grupo_asignaciones: Asignaciones a grupos
"""
#endregion
class Materia(models.Model):

    TIPO_MATERIA_CHOICES = [
        ('TA', 'Taller'),
        ('TE', 'Teoria'),
    ]

    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=2, choices=TIPO_MATERIA_CHOICES, default='OB')
    pid = models.CharField(max_length=30, blank=True)
    cupof = models.PositiveIntegerField(blank=True, null=True)
    fecha_toma_posesion = models.CharField(max_length=30, blank=True)
    forma_ingreso = models.CharField(max_length=30, blank=True)
    horario = models.CharField(max_length=30, blank=True)
    descripcion = models.TextField(blank=True)

    especialidades = models.ManyToManyField(Especialidad, related_name='materias')
    curso = models.ForeignKey(Curso, on_delete=models.PROTECT, related_name='materias')

    def __str__(self):
        return f"{self.nombre} - {self.curso.nombre}"

#region [Documentación Docente]
"""
Profesor o instructor que imparte materias.
Atributos:
  datos personales: nombre, apellido, CUIL, etc.
  datos laborales: legajo, situación de revista
  datos contacto: email, teléfonos
  estado: activo/inactivo
  fecha_ingreso: cuando comenzó
Relaciones:
  carga_academica: Materias asignadas
"""
#endregion
class Docente(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    cuil = models.CharField(max_length=15, unique=True, validators=[RegexValidator(r'^\d{2}-\d{8}-\d{1}$')])
    domicilio = models.CharField(max_length=100, blank=True)
    fecha_nacimiento = models.DateField(blank=True)
    email = models.EmailField(blank=True)
    numero_legajo = models.CharField(max_length=30)
    telefono = models.CharField(max_length=20, blank=True,)
    telefono_alternativo = models.CharField(max_length=20, blank=True)
    situacion_revista = models.CharField(max_length=100, blank=True)
    activo = models.BooleanField(default=True)
    fecha_ingreso = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"

#region [Documentación Alumno]
"""
Estudiante matriculado en la institución.
Atributos:
  datos personales: nombre, DNI, CUIL, etc.
  datos académicos: libro, folio, legajo
  datos contacto: email, teléfono, dirección
  estado: activo/inactivo
Relaciones:
  curso: Curso actual
  especialidad: Especialidad que cursa
  grupo: Grupo asignado
"""
#endregion
class Alumno(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    dni = models.PositiveIntegerField(unique=True, validators=[MinValueValidator(1000000), MaxValueValidator(99999999)])
    cuil = models.CharField(max_length=15, unique=True)
    fecha_nacimiento = models.DateField(blank=True, verbose_name="Fecha de Nacimiento", default="2000-01-01")
    libro = models.CharField(blank=True, max_length=30)
    folio = models.CharField(blank=True, max_length=30,)
    numero_legajo = models.CharField(max_length=30,)
    libro_matriz = models.CharField(blank=True, max_length=30)
    folio_matriz = models.CharField(blank=True, max_length=30)
    email = models.EmailField(blank=True)
    telefono = models.CharField(max_length=20, blank=True)
    domicilio = models.TextField(blank=True)
    activo = models.BooleanField(default=True)
    
    curso = models.ForeignKey(Curso, on_delete=models.PROTECT, null=True, blank=True, related_name='alumnos')
    especialidad = models.ForeignKey(Especialidad, on_delete=models.PROTECT, null=True, blank=True, related_name='alumnos')
    grupo = models.ForeignKey(Grupo, on_delete=models.PROTECT, null=True, blank=True, related_name='alumnos')

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"

    class Meta:
        verbose_name = "Alumno"
        verbose_name_plural = "Alumnos"
        ordering = ['apellido', 'nombre']

#region [Documentación GrupoMateria]
"""
Asignación de materia a grupo con docente.
Atributos:
  horario_inicio: Hora de comienzo
  horario_fin: Hora de finalización
  dias_semana: Días de dictado
Relaciones:
  materia: Materia asignada
  grupo: Grupo específico
  docente: Docente asignado
  aula: Aula designada
"""
#endregion
class GrupoMateria(models.Model):
    horario_inicio = models.TimeField(blank=True)
    horario_fin = models.TimeField(blank=True)
    dias_semana = models.CharField(max_length=20, blank=False)
    aula = models.ForeignKey('Aula', on_delete=models.SET_NULL, null=True, blank=True)

    materia = models.ForeignKey(Materia, on_delete=models.PROTECT, related_name='grupo_asignaciones')
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE, related_name='materia_asignaciones')
    docente = models.ForeignKey(Docente, on_delete=models.PROTECT, null=True, blank=True, related_name='carga_academica')
    
    class Meta:
        unique_together = [['materia', 'grupo']]
        verbose_name = "Asignación de Materia por Grupo"
        verbose_name_plural = "Asignaciones de Materias por Grupo"
        ordering = ['grupo', 'materia']

    def __str__(self):
        docente_nombre = self.docente.__str__() if self.docente else "Sin docente"
        return f"{self.materia.nombre} - {self.grupo.nombre} ({docente_nombre})"

#region [Documentación Aula]
"""
Espacio físico donde se dictan clases.
Atributos:
  nombre: Identificador del aula
  capacidad: Cantidad máxima de alumnos
  tipo: Normal/Laboratorio/Taller
  descripcion: Características adicionales
"""
#endregion
class Aula(models.Model):

    TIPO_AULA_CHOICES = [
        ('NORMAL', 'Aula'),
        ('LAB', 'Laboratorio'),
        ('TALLER', 'Taller'),
        ('SUM', 'S.U.M'),
        ('BIBLIO', 'Biblioteca'),
    ]

    nombre = models.CharField(max_length=50, unique=True)
    capacidad = models.PositiveIntegerField()
    tipo = models.CharField(max_length=10, choices=TIPO_AULA_CHOICES, default='NORMAL')
    descripcion = models.TextField(blank=True)
   

    def __str__(self):
        return f"{self.nombre} ({self.get_tipo_display()}, Cap: {self.capacidad})"

    class Meta:
        verbose_name = "Aula"
        verbose_name_plural = "Aulas"
        ordering = ['nombre']