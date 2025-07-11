from django.db import models # type: ignore
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator # type: ignore
from django.core.exceptions import ValidationError # type: ignore



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


class Aula(models.Model):
    TIPO_AULA_CHOICES = [
        ('AULA', 'Aula'),
        ('LAB.', 'Laboratorio'),
        ('S.U.M', 'S.U.M'),
        ('BIBLIO.', 'Biblioteca'),
    ]

    nombre = models.CharField(max_length=50, unique=True)
    capacidad = models.PositiveIntegerField()
    tipo = models.CharField(max_length=10, choices=TIPO_AULA_CHOICES, default='AULA')
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

class Grupo(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

class Especialidad(models.Model):
    nombre = models.CharField(unique=True, max_length=100)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

class Turno(models.Model):
    nombre = models.CharField(unique=True, max_length=50)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return f"{self.nombre} ({self.hora_inicio.strftime('%H:%M')}-{self.hora_fin.strftime('%H:%M')})"

class Curso(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        #return f"{self.nombre} - Año {self.año}"
        return f"{self.nombre}"

class Materia(models.Model):

    TIPO_MATERIA_CHOICES = [
        ('TALLER', 'Taller'),
        ('TEORIA', 'Teoria'),
    ]

    TIPO_INGRESO_CHOICES = [
        ('M.A.D', 'MAD'),
        ('REUBICADO', 'REUBICADO'),
        ('APD', 'ACTO PUBLICO DIGITAL'),
        ('AP', 'ACTO PUBLICO'),
        ('DD', 'DESTINO DEFINITIVO'),
        ('PN', 'PROPUESTA NOMBRAMIENTO'),
        ('PE', 'PROYECTO Y ELECCION'),
        ('DIS', 'DISPOSICION'),
        ('OTROS', 'OTROS'),
    ]

    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20, choices=TIPO_MATERIA_CHOICES, default='TEORIA')
    pid = models.CharField(max_length=30, blank=True)
    cupof = models.PositiveIntegerField(blank=True, null=True)
    fecha_toma_posesion = models.CharField(max_length=30, blank=True)
    forma_ingreso = models.CharField(max_length=30, choices=TIPO_INGRESO_CHOICES, default='ACTO PUBLICO DIGITAL')
    secuencia= models.CharField(max_length=20, blank=True)
    horario_inicio = models.TimeField(blank=True, default="12:00")
    horario_fin = models.TimeField(blank=True, default="12:00")
    dias_semana = models.CharField(max_length=20, blank=False, default='')
    descripcion = models.TextField(blank=True)
    numero_dispo = models.CharField(max_length=100, blank=True, null=True)
    

    aula = models.ForeignKey(Aula, on_delete=models.SET_NULL, null=True, blank=True)
    curso = models.ForeignKey(Curso, on_delete=models.PROTECT, related_name='curso')
    especialidades = models.ManyToManyField(Especialidad, related_name='especialidad')

    def __str__(self):
        return f"{self.nombre} - {self.curso.nombre}"

class Docente(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    cuil = models.CharField(max_length=15, unique=True, validators=[RegexValidator(r'^\d{2}-\d{8}-\d{1}$')])
    domicilio = models.CharField(max_length=100, blank=True)
    fecha_nacimiento = models.DateField(blank=True)
    email = models.EmailField(blank=True)
    numero_legajo = models.CharField(max_length=30)
    telefono = models.CharField(max_length=20, blank=True,)
    telefono_emergencia = models.CharField(max_length=20, blank=True,)
    fecha_ingreso = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"

class GrupoMateria(models.Model):
      
    SIT_DE_REVISTA = [
        
        ('SUPLENTE', 'SUPLENTE'),
        ('PROVISIONAL', 'PROVISIONAL'),
        ('TITULAR INT.', 'TITULAR_INT'),
        ('TITULAR', 'TITULAR'),

    ]
      
    situacion_revista = models.CharField(max_length=100, choices=SIT_DE_REVISTA, default='SUPLENTE')

    materia = models.ForeignKey(Materia, on_delete=models.PROTECT, related_name='grupo_asignaciones')
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE, related_name='materia_asignaciones')
    docente = models.ForeignKey(Docente, on_delete=models.PROTECT, null=True, blank=True, related_name='carga_academica')

    def clean(self):
        # Solo validamos si ya se asignaron materia y grupo
        if not self.materia_id or not self.grupo_id:
            return

        # Buscamos si ya existe una asignación con mismo grupo, materia.nombre y materia.curso
        if GrupoMateria.objects.exclude(pk=self.pk).filter(
            grupo=self.grupo,
            materia__nombre=self.materia.nombre,
            materia__curso=self.materia.curso
        ).exists():
            raise ValidationError("Ya existe una asignación con el mismo nombre de materia, curso y grupo.")

    class Meta:
        unique_together = [['materia', 'grupo','docente']]
        verbose_name = "Asignación de Materia por Grupo"
        verbose_name_plural = "Asignaciones de Materias por Grupo"
        ordering = ['grupo', 'materia']

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

class TipoCargo(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

class Cargo(models.Model):
    docente = models.ForeignKey(Docente, on_delete=models.SET_NULL, null=True, blank=True, related_name='cargos')
    cargo = models.ForeignKey(TipoCargo, on_delete=models.SET_NULL, null=True)
    curso = models.ManyToManyField(Curso, blank=True, related_name='curso_cargo')
    especialidades = models.ForeignKey(Especialidad, on_delete=models.SET_NULL, blank=True, null=True, related_name='especialidad_cargo')

    def __str__(self):
        return f"{self.cargo}, {self.docente}"