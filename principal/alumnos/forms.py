from django import forms # type: ignore
from .models import Alumno, AlumnoDatos, Especialidad, Turno, Curso, Docente, Grupo, GrupoMateria, Materia, Cargo
import re

from django.core.validators import FileExtensionValidator # type: ignore

# DOCENTE

class DocenteForm(forms.ModelForm):

    class Meta:
        model = Docente
        fields = [
            'nombre',
            'apellido',
            'cuil',
            'fecha_nacimiento',
            'numero_legajo',
            'email',
            'telefono',
            'domicilio',
            'telefono_emergencia', 
            'fecha_ingreso',
        ]
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super(DocenteForm, self).__init__(*args, **kwargs)
        
        fecha_widget = forms.DateInput(
            attrs={
                'type': 'date',
                'class': 'form-control',
            },
            format='%Y-%m-%d',
        )

# ALUMNO

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ['nombre', 'apellido', 'dni', 'cuil', 'fecha_nacimiento', 'libro', 'folio', 'numero_legajo', 'libro_matriz', 'folio_matriz', 'email', 'telefono', 'domicilio', 'activo', 'curso', 'especialidad','grupo']

    # Sobrescribimos el widget para el campo 'fecha_nacimiento'
    def __init__(self, *args, **kwargs):
        super(AlumnoForm, self).__init__(*args, **kwargs)
        self.fields['fecha_nacimiento'].widget = forms.DateInput(
            attrs={
                'type': 'date',  # Input HTML5 tipo fecha
                'class': 'form-control',
            },
            format='%Y-%m-%d',  # Formato esperado por HTML5 (yyyy-MM-dd)
        )


    def clean_dni(self):
        dni = self.cleaned_data['dni']
        if not str(dni).isdigit():
            raise forms.ValidationError("El DNI debe contener solo números.")
        return dni

class AlumnoUploadFileForm(forms.Form):

    #Formulario para subir archivos Excel con validación de extensión
    
    file = forms.FileField(
        label='Archivo Excel',
        help_text='El archivo debe tener las columnas: Nombre, Apellido, DNI, CUIL, Fecha Nacimiento, Libro, Folio, Número de Legajo, Libro Matriz, Folio Matriz ,Curso, Especialidad, Grupo',
        validators=[FileExtensionValidator(allowed_extensions=['xlsx', 'xls'])]
    )

class AlumnoDatosForm(forms.ModelForm):

    # region Sección CHOISES

    POSEE_DNI_CHOICES = [
        ("fisico", "Sí, y tiene DNI físico"),
        ("tramite", "Sí, pero no tiene el DNI físico y se encuentra en trámite"),
        ("sin_tramite", "Sí, pero no tiene el DNI físico y no se encuentra en trámite"),
        ("no_posee", "No posee DNI argentino"),
    ]

    IDENTIDAD_GENERO_CHOICES = [
        ("mujer", "Mujer"),
        ("mujer_trans", "Mujer trans"),
        ("varon", "Varón"),
        ("varon_trans", "Varón trans"),
        ("no_binario", "No binario"),
        ("otra", "Otra"),
        ("no_responde", "Prefiere no responder"),
    ]

    MEDIOS_TRANSPORTE = [
        ("a_pie_bicicleta", "A pie / Bicicleta"),
        ("transporte_escolar", "Transporte escolar (DGCyE)"),
        ("colectivo", "Colectivo"),
        ("tren", "Tren"),
        ("vehiculo_particular", "Vehículo particular"),
        ("taxi_remis", "Taxi / Remis"),
        ("otros", "Otros"),
    ]

    CONDICIONES_SALUD_IZQ = [
        ("asma_bronco", "Asma / Broncoespasmo a repeticion"),
        ("celiaquia", "Celiaquia"),
        ("prob_cardio", "Problemas / Condiciones cardiacas"),
        ("diabetes", "Diabetes"),
        ("pres_arterial", "Presion arterial elevada"),
        ("convulciones", "Convulciones"),
        ("alt_sanguineas", "Alteraciones sanguineas"),
        ("quem_se_mod", "Quemaduras severas o moderadas"),
    ]

    CONDICIONES_SALUD_DER = [
        ("falla_organo", "Falla o no funcionamiento de algun organo"),
        ("enf_oncohema", "Enfermedad oncohematologica"),
        ("inmuno", "Inmunodeficiencias (bajas defensas) por enfermedad o medicamentos"),
        ("frac_lux_lesiones", "Fracturas, luxaciones, lesiones ligamentarias previas"),
        ("prpb_huesos", "Otro problema en los huesos o articulacioes"),
        ("trau_craneo", "Traumatismo de craneo que haya requerido observacion por guardia o internacion"),
        ("prob_piel", "Problemas de piel"),
    ]

    EJERCICIO_IZQ = [
        ("desmayos", "Desmayos"),
        ("dolor_pecho", "Dolor fuerte en el pecho"),
        ("mareos", "Mareos"),
    ]

    EJERCICIO_DER = [
        ("may_cansancio", "Mayor cansancio que sus compañeros"),
        ("palpita", "Palpitaciones"),
        ("dif_resp", "Dificultad para respirardurante o despues de la actividad fisica"),
    ]

    INTERNACION_IZQ = [
        ("int_com", "Internacion en sala comun"),
        ("int_cuid_int", "Internacion en sala de cuidados intermedios/intensivos"),
    ]

    ALERGIAS_IZQ = [
        ("medicamentos", "Medicamentos"),
        ("vacunas", "Vacunas"),
        ("alimentos", "Alimentos"),
    ]

    ALERGIAS_DER = [
        ("picaduras", "Picaduras de insectos"),
        ("estacionales", "Estacionales(Polen,acaros,polvo,etc)"),
        ("otras", "Otras"),
    ]

    ANTECEDENTES_SALUD_IZQ = [
        ("muerte_subita", "Muerte súbita de un familiar directo menor de 50 años"),
        ("diab", "Diabetes"),
        ("prob_card", "Problemas cardíacos"),
    ]

    ANTECEDENTES_SALUD_DER = [
        ("tos_cron", "Tos crónica"),
        ("celia", "Celiaquía"),
    ]

    DEPENDENCIAS = [
        ("oficial", "Oficial"),
        ("muni", "Municipal"),
        ("nacio", "Nacional"),
        ("priva", "Privada"),
        ("o_orgas", "Otros organismos"),
    ]

    ESC_CURSA = [
        ("concu", "Concurre a una Escuela Especial a contraturno y cuenta con acompañamiento de maestra o maestro de inclusión "),
        ("noconcu", "No concurre a una Escuela Especial pero cuenta con acompañamiento de maestra o maestro de inclusión"),
    ]

    INS_EN = [
        ("cb", "Ciclo Básico"),
        ("cs", "Ciclo Superior"),
        ("af", "Aula de Fortalecimiento"),
        ("eps", "Escuela Profesional Secundaria"),
    ]

    ANOO = [
        ("uno", "1"),
        ("dos", "2"),
        ("tres", "3"),
        ("cuatro", "4"),
        ("cinco", "5"),
        ("seis", "6"),
        ("siete", "7"),
    ]

    TURNOS = [
        ("man", "Mañana"),
        ("tar", "Tarde"),
        ("ves", "Vespertino"),
        ("noc", "Noche"),
    ]

    JORNADAS = [
        ("sim", "Simple"),
        ("ext", "Extendida"),
        ("comp", "Completa/Doble Escolaridad"),

    ]

    INS_ACTUAL = [
        ("in", "Ingresante al Nivel"),
        ("pp", "Promovida / Promovido"),
        ("rr", "Reinscripta / Reinscripto"),
        ("rep", "Repitente"),

    ]

    VINCULO = [
        ("mad", "Madre"),
        ("pad", "Padre"),
        ("tut", "Tutor"),
        ("tuto", "Tutora"),
        ("otr", "Otro"),

    ]

    POSEE_DNI_CHOICES2 = [
        ("sit", "Sí, y tiene DNI físico"),
        ("sin", "Sí, pero no tiene el DNI físico"),
        ("not", "No posee DNI argentino"),
    ]

    NIVEL_Q_CURSO = [
        ("pri", "Primario"),
        ("sec", "Secundario"),
        ("sup", "Superior"),
        ("supu", "Superior Universitario"),
        ("pos", "Posgrado"),
    ]

    CONDICIÓN_DE_ACTIVIDAD = [
        ("est", "Estudia"),
        ("tra", "Trabaja"),
        ("butra", "Busca trabajo"),
        ("rtcnp", "Realiza tareas de cuidado no pagas"),
        ("rjp", "Recibe jubilación o pensión"),
    ]




    #endregion


    # region Sección DATOS ESTUDIANTES

    apellido = forms.CharField(label="Apellido/s", max_length=100)
    
    nombre = forms.CharField(label="Nombre/s", max_length=100)
    
    fecha_nacimiento = forms.DateField(
        label="Fecha de nacimiento",
        widget=forms.DateInput(attrs={"type": "date"})
    )

    posee_dni = forms.ChoiceField(
        choices=POSEE_DNI_CHOICES,
        widget=forms.RadioSelect,
        required=False
    )

    cpi = forms.ChoiceField(
        choices=[("si", "Sí"), ("no", "No")],
        widget=forms.RadioSelect,
        label="¿Posee certificado de Pre-identificación (CPI)?",
        required=False,
    )

    doc_extranjero = forms.ChoiceField(
        label="¿Posee documento extranjero?",
        choices=[("si", "Sí"), ("no", "No")],
        widget=forms.RadioSelect,
        required=False,
    )

    tipo_doc_extranjero = forms.CharField(
        label="Tipo",
        max_length=50,
        required=False,
    )

    num_doc_extranjero = forms.CharField(
        label="Número",
        max_length=50,
        required=False,
    )

    num_dni = forms.CharField(
    label="Número de DNI",
    max_length=20,
    required=False,
    )

    cuil = forms.CharField(
    label="CUIL",
    max_length=20,
    required=False,
    ) 

    identidad_genero = forms.ChoiceField(
        choices=IDENTIDAD_GENERO_CHOICES,
        widget=forms.RadioSelect,
        required=False
    )

    identidad_genero_otra = forms.CharField(
    label="Especifique otra identidad de género",
    required=False,
    max_length=100,
    )

    lugar_nacimiento = forms.ChoiceField(
        choices=[("argentina", "En Argentina"), ("extranjero", "En el extranjero")],
        widget=forms.RadioSelect,
        label="Lugar de nacimiento",
    )

    nacionalidad = forms.CharField(
        required=False,
        label="Nacionalidad (si nació en el extranjero)"
    )

    nac_argentina_opcion = forms.ChoiceField(
        choices=[("buenos_aires", "Buenos Aires"), ("otra", "Otra provincia")],
        widget=forms.RadioSelect,
        required=False,
        label="Provincia de nacimiento"
    )
    
    provincia = forms.CharField(required=False, label="Provincia (si no es Buenos Aires)")

    distrito = forms.CharField(required=False)
    localidad = forms.CharField(required=False)
    calle = forms.CharField(required=False)
    numero = forms.CharField(required=False, label="Número")
    piso = forms.CharField(required=False)
    torre = forms.CharField(required=False)
    departamento = forms.CharField(required=False)
    entre_calle = forms.CharField(required=False, label="Entre calle")
    y_calle = forms.CharField(required=False, label="Y calle")
    otro_dato = forms.CharField(required=False, label="Otro dato")
    telefono = forms.CharField(required=False, label="Teléfono")
    telefono_celular = forms.CharField(required=False, label="Teléfono celular") 

    tiene_hermanos = forms.ChoiceField(
        label="¿Hermanas o hermanos?",
        choices=[("si", "Sí"), ("no", "No")],
        widget=forms.RadioSelect,
        required=False,
    )

    cantidad_hermanos = forms.IntegerField(
        required=False,
        label="Cantidad de Hermanos/as",
    )

    hermanos_en_institucion = forms.IntegerField(
        required=False,
        label="Cuantos en esta Intitución",
    )

    idioma_hogar = forms.ChoiceField(
        label="¿Se hablan distintas lenguas en el hogar?",
        choices=[("si", "Sí"), ("no", "No")],
        widget=forms.RadioSelect,
        required=False,
    )

    leng_indigenas = forms.ChoiceField(
        label="¿Lengua/s indigena/s?",
        choices=[("si", "Sí"), ("no", "No")],
        widget=forms.RadioSelect,
        required=False,
    )

    otras_leng = forms.ChoiceField(
        label="¿Otras lenguas?",
        choices=[("si", "Sí"), ("no", "No")],
        widget=forms.RadioSelect,
        required=False,
    )

    des_porg = forms.ChoiceField(
        label="¿Se reconoce perteneciente o descendiente de pueblos originarios?",
        choices=[("si", "Sí"), ("no", "No")],
        widget=forms.RadioSelect,
        required=False,
    )

    per_auh = forms.ChoiceField(
        label="¿Persive Asignacion Universal por hijo (AUH)?",
        choices=[("si", "Sí"), ("no", "No")],
        widget=forms.RadioSelect,
        required=False,
    )

    per_prog = forms.ChoiceField(
        label="¿Persive plan PROGRESAR?",
        choices=[("si", "Sí"), ("no", "No")],
        widget=forms.RadioSelect,
        required=False,
    )

    medio_transporte = forms.MultipleChoiceField(
        label="Medio de transporte que utiliza para llegar al establecimiento",
        choices=MEDIOS_TRANSPORTE,
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    tiene_hijos = forms.ChoiceField(
        label="¿Tiene hijas o hijos menosres de 3 años?",
        choices=[("si", "Sí"), ("no", "No")],
        widget=forms.RadioSelect,
        required=False,
    )

    asiste_maternales = forms.ChoiceField(
        label="¿Asisten a una sala del Proyecto de Salas Maternales?",
        choices=[("si", "Sí"), ("no", "No")],
        widget=forms.RadioSelect,
        required=False,
    )

    # endregion

    # region Sección INFORMACION SALUD

    obra_social = forms.ChoiceField(
        label="¿Posee obra social?",
        choices=[("si", "Sí"), ("no", "No")],
        widget=forms.RadioSelect,
        required=False,
    )

    obrsoc = forms.CharField(
    label="Obra Social",
    max_length=20,
    required=False,
    )

    n_afil = forms.CharField(
    label="Numero de afiliado",
    max_length=20,
    required=False,
    )

    info_salud_izq = forms.MultipleChoiceField(
        choices=CONDICIONES_SALUD_IZQ,
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    info_salud_der = forms.MultipleChoiceField(
        choices=CONDICIONES_SALUD_DER,
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    ejercicio_izq = forms.MultipleChoiceField(
        choices=EJERCICIO_IZQ,
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    ejercicio_der = forms.MultipleChoiceField(
        choices=EJERCICIO_DER,
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    int_comun = forms.ChoiceField(
        label="¿Internacion en sala comun?",
        choices=[("si", "Sí"), ("no", "No")],
        widget=forms.RadioSelect,
        required=False,
    )

    cuantas_veces = forms.CharField(
    label="¿Cuantas veces?",
    max_length=20,
    required=False,
    )

    causas_diag = forms.CharField(
    label="Indique la/s causa/s o diagnostico/s",
    max_length=100,
    required=False,
    )

    int_int = forms.ChoiceField(
        label="¿Internacion en sala de cuidados intermedios/intensivos?",
        choices=[("si", "Sí"), ("no", "No")],
        widget=forms.RadioSelect,
        required=False,
    )

    cuantas_veces_2 = forms.CharField(
    label="¿Cuantas veces?",
    max_length=20,
    required=False,
    )

    causas_diag_2 = forms.CharField(
    label="Indique la/s causa/s o diagnostico/s",
    max_length=100,
    required=False,
    )

    aler_graves = forms.ChoiceField(
        label="¿Padece o ha padecido algun tipo de alergia grave? (Indique si requirio internacion)",
        choices=[("si", "Sí"), ("no", "No")],
        widget=forms.RadioSelect,
        required=False,
    )

    alergias_izq = forms.MultipleChoiceField(
        choices=ALERGIAS_IZQ,
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    alergias_der = forms.MultipleChoiceField(
        choices=ALERGIAS_DER,
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    medicamentos_confirma = forms.ChoiceField(
        choices=[("si", "Sí"), ("no", "No")],
        widget=forms.RadioSelect,
        required=False,
    )

    vacunas_confirma = forms.ChoiceField(
        choices=[("si", "Sí"), ("no", "No")],
        widget=forms.RadioSelect,
        required=False,
    )

    alimentos_confirma = forms.ChoiceField(
        choices=[("si", "Sí"), ("no", "No")],
        widget=forms.RadioSelect,
        required=False,
    )

    picaduras_confirma = forms.ChoiceField(
        choices=[("si", "Sí"), ("no", "No")],
        widget=forms.RadioSelect,
        required=False,
    )

    estacionales_confirma = forms.ChoiceField(
        choices=[("si", "Sí"), ("no", "No")],
        widget=forms.RadioSelect,
        required=False,
    )

    otras_confirma = forms.ChoiceField(
        choices=[("si", "Sí"), ("no", "No")],
        widget=forms.RadioSelect,
        required=False,
    )

    dis_auditiva = forms.ChoiceField(
        label="¿Tiene disminución auditiva?",
        choices=[("si", "Sí"), ("no", "No")],
        widget=forms.RadioSelect,
        required=False,
    )

    usa_audifono = forms.ChoiceField(
        choices=[("si", "Sí"), ("no", "No")],
        widget=forms.RadioSelect,
        required=False,
    )

    dis_visual = forms.ChoiceField(
        label="¿Tiene disminución visual?",
        choices=[("si", "Sí"), ("no", "No")],
        widget=forms.RadioSelect,
        required=False,
    )

    usa_lentes = forms.ChoiceField(
        label="¿Usa lentes?",
        choices=[("si", "Sí"), ("no", "No")],
        widget=forms.RadioSelect,
        required=False,
    )

    recive_med = forms.ChoiceField(
        label="¿Recibe de manera habitual algún tipo de medicación?",
        choices=[("si", "Sí"), ("no", "No")],
        widget=forms.RadioSelect,
        required=False,
    )

    cual_med = forms.CharField(
    label="¿Cual?",
    max_length=20,
    required=False,
    )

    alg_op = forms.ChoiceField(
        label="¿Tuvo alguna operación?",
        choices=[("si", "Sí"), ("no", "No")],
        widget=forms.RadioSelect,
        required=False,
    )

    xq_motivo = forms.CharField(
    label="¿Porque motivo?",
    max_length=20,
    required=False,
    )

    en_que_year = forms.CharField(
    label="¿En que año?",
    max_length=20,
    required=False,
    )

    ant_salud_izq = forms.MultipleChoiceField(
        choices=ANTECEDENTES_SALUD_IZQ,
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    ant_salud_der = forms.MultipleChoiceField(
        choices=ANTECEDENTES_SALUD_DER,
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )


    
   


    # endregion

    #region Sección DATOS ESTABLECIMIENTO

    distrito_esta = forms.CharField(
    label="Distrito",
    max_length=20,
    required=False,
    )

    nom_escuela = forms.CharField(
    label="Nombre de la escuela",
    max_length=20,
    required=False,
    )

    numero_esta = forms.CharField(
    label="Nº",
    max_length=20,
    required=False,
    )

    cue = forms.CharField(
    label="CUE",
    max_length=20,
    required=False,
    )

    clave_prov = forms.CharField(
    label="Clave provincial",
    max_length=20,
    required=False,
    )

    sector_pp = forms.ChoiceField(
        label="Sector de gestión",
        choices=[("privado", "Privado"), ("publico", "Publico")],
        widget=forms.RadioSelect,
        required=False,
    )

    sector_pp_2 = forms.ChoiceField(
        label="País",
        choices=[("argentina", "Argentina"), ("otrop", "Otro país")],
        widget=forms.RadioSelect,
        required=False,
    )

    esp_pais = forms.CharField(
    label="País",
    max_length=20,
    required=False,
    )

    distrito_proc = forms.CharField(
    label="Distrito",
    max_length=20,
    required=False,
    )

    nom_escuela_proc = forms.CharField(
    label="Nombre de la escuela",
    max_length=20,
    required=False,
    )

    numero_proc = forms.CharField(
    label="Nº",
    max_length=20,
    required=False,
    )

    nivel_mod = forms.CharField(
    label="Nivel/Modalidad",
    max_length=20,
    required=False,
    )

    sector_pp_3 = forms.ChoiceField(
        label="Sector de gestión",
        choices=[("privado", "Privado"), ("publico", "Publico")],
        widget=forms.RadioSelect,
        required=False,
    )

    dependencias = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'd-inline-flex gap-3'}),
        choices=DEPENDENCIAS,
        required=False,
    )

    select_prov = forms.ChoiceField(
        label="Provincia",
        choices=[("bs", "Buenos Aires"), ("otrap2", "Otra Provincia")],
        widget=forms.RadioSelect,
        required=False,
    )

    prov_4 = forms.CharField(
        label="Provincia",
        max_length=20,
        required=False,
    )


    #endregion  

    #region Sección INSCRIPCIÓN

    cursa_p_inclu = forms.ChoiceField(
        label="¿Cursa con proyecto de inclusión?",
        choices=[("si", "Sí"), ("no", "No")],
        widget=forms.RadioSelect,
        required=False,
    )

    esc_cursa = forms.ChoiceField(
        label="Marque con una cruz lo que corresponda",
        choices=ESC_CURSA,
        widget=forms.RadioSelect,
        required=False,
    )

    tiene_acomp = forms.ChoiceField(
        label="¿Cursa con acompañante asistente externo?",
        choices=[("si", "Sí"), ("no", "No")],
        widget=forms.RadioSelect,
        required=False,
    )

    ins_en = forms.ChoiceField(
        label="Se inscribe en",
        choices=INS_EN,
        widget=forms.RadioSelect(attrs={'class': 'd-inline-flex gap-3'}),
        required=False,
    )

    orient = forms.CharField(
        label="Orientación",
        max_length=100,
        required=False,
    )


    anoo = forms.ChoiceField(
        label="Año",
        choices=ANOO,
        widget=forms.RadioSelect(attrs={'class': 'd-inline-flex gap-3'}),
        required=False,
    )

    tur = forms.ChoiceField(
        label="Turno solicitado",
        choices=TURNOS,
        widget=forms.RadioSelect(attrs={'class': 'd-inline-flex gap-3'}),
        required=False,
    )

    jornadas = forms.ChoiceField(
        label="Jornada",
        choices=JORNADAS,
        widget=forms.RadioSelect(attrs={'class': 'd-inline-flex gap-3'}),
        required=False,
    )

    ins_act = forms.ChoiceField(
        choices=INS_ACTUAL,
        widget=forms.RadioSelect(attrs={'class': 'd-inline-flex gap-3'}),
        required=False,
    )




    #endregion  

    #region Sección EDUCACIÓN COMPLEMENTARIA

    asis_inst = forms.ChoiceField(
        label="Centro Educativo Complementario (CEC)",
        choices=[("si", "Sí"), ("no", "No")],
        widget=forms.RadioSelect,
        required=False,
    )

    asis_inst_2 = forms.ChoiceField(
        label="Centro de Educación Física (CEF)",
        choices=[("si", "Sí"), ("no", "No")],
        widget=forms.RadioSelect,
        required=False,
    )

    asis_inst_3 = forms.ChoiceField(
        label="Escuela de Educación Estética",
        choices=[("si", "Sí"), ("no", "No")],
        widget=forms.RadioSelect,
        required=False,
    )


    incorp_serv_esc = forms.MultipleChoiceField(
        label="¿Solicita la incorporación en el Servicio Alimentario Escolar?",
        choices=[("comedor", "Comedor"), ("desmer", "Desayuno/Merienda")],
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )



    #endregion

    #region Sección ADULTO RESPONSABLE

    vinc_est = forms.ChoiceField(
        label="Vínculo con estudiante",
        choices=VINCULO,
        widget=forms.RadioSelect(attrs={'class': 'd-inline-flex gap-3'}),
        required=False,
    )

    vinc_est2 = forms.ChoiceField(
        label="Vínculo con estudiante",
        choices=VINCULO,
        widget=forms.RadioSelect(attrs={'class': 'd-inline-flex gap-3'}),
        required=False,
    )

    ape_adul_1 = forms.CharField(
        label="Apellido",
        max_length=20,
        required=False,
    )

    nombre_adul_1 = forms.CharField(
        label="Nombre",
        max_length=20,
        required=False,
    )

    nac_adul_1 = forms.CharField(
        label="Nacionalidad",
        max_length=20,
        required=False,
    )

    ape_adul_2 = forms.CharField(
        label="Apellido",
        max_length=20,
        required=False,
    )

    nombre_adul_2 = forms.CharField(
        label="Nombre",
        max_length=20,
        required=False,
    )

    nac_adul_2 = forms.CharField(
        label="Nacionalidad",
        max_length=20,
        required=False,
    )

    dni_adul_1 = forms.ChoiceField(
        label="¿Posee DNI argentino? ",
        choices=POSEE_DNI_CHOICES2,
        widget=forms.RadioSelect,
        required=False,
    )

    dni_adul_2 = forms.ChoiceField(
        label="¿Posee DNI argentino? ",
        choices=POSEE_DNI_CHOICES2,
        widget=forms.RadioSelect,
        required=False,
    )

    ndoc_adul_1 = forms.CharField(
        label="Numero",
        max_length=50,
        required=False,
    )

    ndoc_adul_2 = forms.CharField(
        label="Numero",
        max_length=50,
        required=False,
    )

    po_cdi = forms.ChoiceField(
        label="¿Posee Certificado de Pre-Identificación (CPI)?",
        choices=[("si", "Sí"), ("no", "No")],
        widget=forms.RadioSelect,
        required=False,
    )

    po_cdi2 = forms.ChoiceField(
        label="¿Posee Certificado de Pre-Identificación (CPI)?",
        choices=[("si", "Sí"), ("no", "No")],
        widget=forms.RadioSelect,
        required=False,
    )

    doc_extra1 = forms.ChoiceField(
        label="¿Posee documento extranjero?",
        choices=[("si", "Sí"), ("no", "No")],
        widget=forms.RadioSelect,
        required=False,
    )

    doc_extra2 = forms.ChoiceField(
        label="¿Posee documento extranjero?",
        choices=[("si", "Sí"), ("no", "No")],
        widget=forms.RadioSelect,
        required=False,
    )

    ndoc_adul_extra_1 = forms.CharField(
        label="Numero",
        max_length=100,
        required=False,
    )

    ndoc_adul_extra_2 = forms.CharField(
        label="Numero",
        max_length=100,
        required=False,
    )

    prof_edu_1 = forms.CharField(
        label="Profesión u ocupación",
        max_length=100,
        required=False,
    )

    prof_edu_2 = forms.CharField(
        label="Profesión u ocupación",
        max_length=100,
        required=False,
    )

    asis_esta_edu_adul_1 = forms.ChoiceField(
        label="¿Asistió a algún establecimiento educativo?",
        choices=[("si", "Sí"), ("no", "No")],
        widget=forms.RadioSelect,
        required=False,
    )

    asis_esta_edu_adul_2 = forms.ChoiceField(
        label="¿Asistió a algún establecimiento educativo?",
        choices=[("si", "Sí"), ("no", "No")],
        widget=forms.RadioSelect,
        required=False,
    )

    niv_curso_1 = forms.ChoiceField(
        label=" ¿Cuál es el nivel más alto que cursó?",
        choices=NIVEL_Q_CURSO,
        widget=forms.RadioSelect,
        required=False,
    )

    niv_curso_2 = forms.ChoiceField(
        label=" ¿Cuál es el nivel más alto que cursó?",
        choices=NIVEL_Q_CURSO,
        widget=forms.RadioSelect,
        required=False,
    )

    comp_niv_1 = forms.ChoiceField(
        label="¿Completó ese nivel?",
        choices=[("si", "Sí"), ("no", "No")],
        widget=forms.RadioSelect,
        required=False,
    )

    comp_niv_2 = forms.ChoiceField(
        label="¿Completó ese nivel?",
        choices=[("si", "Sí"), ("no", "No")],
        widget=forms.RadioSelect,
        required=False,
    )

    con_act_1 = forms.ChoiceField(
        choices=CONDICIÓN_DE_ACTIVIDAD,
        widget=forms.RadioSelect,
        required=False,
    )

    con_act_2 = forms.ChoiceField(
        choices=CONDICIÓN_DE_ACTIVIDAD,
        widget=forms.RadioSelect,
        required=False,
    )

    vive_est_1 = forms.ChoiceField(
        label="¿Convive con la o el estudiante?",
        choices=[("si", "Sí"), ("no", "No")],
        widget=forms.RadioSelect,
        required=False,
    )

    vive_est_2 = forms.ChoiceField(
        label="¿Convive con la o el estudiante?",
        choices=[("si", "Sí"), ("no", "No")],
        widget=forms.RadioSelect,
        required=False,
    )

    calle_f_1 = forms.CharField(required=False, label="Calle")
    numero_f_1 = forms.CharField(required=False, label="Número")
    piso_f_1 = forms.CharField(required=False, label="Piso")
    torre_f_1 = forms.CharField(required=False, label="Torre")
    departamento_f_1 = forms.CharField(required=False, label="Departamento")
    entre_calle_f_1 = forms.CharField(required=False, label="Entre calle")
    y_calle_f_1 = forms.CharField(required=False, label="Y calle")
    otro_dato_f_1 = forms.CharField(required=False, label="Otro dato")
    provincia_f_1 = forms.CharField(required=False, label="Provincia")
    distrito_f_1 = forms.CharField(required=False, label="Distrito")
    localidad_f_1 = forms.CharField(required=False, label="Localidad")
    telefono_f_1 = forms.CharField(required=False, label="Teléfono")
    telefono_celular_f_1 = forms.CharField(required=False, label="Teléfono celular")
    email_f_1 = forms.CharField(required=False, label="E-mail")

    calle_f_2 = forms.CharField(required=False, label="Calle")
    numero_f_2 = forms.CharField(required=False, label="Número")
    piso_f_2 = forms.CharField(required=False, label="Piso")
    torre_f_2 = forms.CharField(required=False, label="Torre")
    departamento_f_2 = forms.CharField(required=False, label="Departamento")
    entre_calle_f_2 = forms.CharField(required=False, label="Entre calle")
    y_calle_f_2 = forms.CharField(required=False, label="Y calle")
    otro_dato_f_2 = forms.CharField(required=False, label="Otro dato")
    provincia_f_2 = forms.CharField(required=False, label="Provincia")
    distrito_f_2 = forms.CharField(required=False, label="Distrito")
    localidad_f_2 = forms.CharField(required=False, label="Localidad")
    telefono_f_2 = forms.CharField(required=False, label="Teléfono")
    telefono_celular_f_2 = forms.CharField(required=False, label="Teléfono celular")
    email_f_2 = forms.CharField(required=False, label="E-mail")
    
    
    ape_f = forms.CharField(
        label="Apellido/s",
        max_length=100,
        required=False,
    )

    nomb_f = forms.CharField(
        label="Nombre/s",
        max_length=100,
        required=False,
    )

    tipo_f = forms.CharField(
        label="Tipo de doc",
        max_length=100,
        required=False,
    )

    num_f = forms.CharField(
        label="Numero",
        max_length=100,
        required=False,
    )

    des_f = forms.CharField(
        label="Describa restricción",
        max_length=400,
        required=False,
    )
     



    #endregion


    #region Funciones y Meta

    class Meta:
        model = AlumnoDatos
        fields = '__all__'

        widgets = {
            'medicamentos_confirma': forms.RadioSelect(attrs={'class': 'form-check-inline'}),
            'fecha': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date', 'class': 'form-control'}),
        }

        def __init__(self, *args, **kwargs):
            super(AlumnoDatosForm, self).__init__(*args, **kwargs)
            # Asegurar que Django acepte el formato YYYY-MM-DD al procesar el input
            self.fields['fecha'].input_formats = ['%Y-%m-%d']



    def clean_cuil(self):
        cuil = self.cleaned_data.get("cuil")
        posee_dni = self.cleaned_data.get("posee_dni")
        if posee_dni != "no_posee" and cuil:
            if not re.match(r"^\d{2}-\d{8}-\d{1}$", cuil):
                raise forms.ValidationError("El CUIL debe tener el formato ##-########-#.")
        return cuil
    
    #endregion

# ESPECIALIDADES

class EspecialidadForm(forms.ModelForm):
    class Meta:
        model = Especialidad
        fields = ['nombre', 'descripcion']

# TURNOS

class TurnoForm(forms.ModelForm):
    class Meta:
        model = Turno
        fields = ['nombre', 'hora_inicio', 'hora_fin', 'descripcion']
        widgets = {
            'hora_inicio': forms.TimeInput(attrs={'type': 'time'}),
            'hora_fin': forms.TimeInput(attrs={'type': 'time'}),
        }

# CURSOS

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nombre',]


    def clean(self):
        cleaned_data = super().clean()
        nombre = cleaned_data.get("nombre")

        return cleaned_data

# GRUPOS

class GrupoForm(forms.ModelForm):

    class Meta:
        model = Grupo
        fields = ['nombre', 'descripcion']

# MATERIA

class MateriaForm(forms.ModelForm):
    class Meta:
        model = Materia
        fields = '__all__'

class GrupoMateriaForm(forms.ModelForm):
    class Meta:
        model = GrupoMateria
        fields = ['grupo', 'docente', 'situacion_revista']

from django.conf import settings



#CARGO
class CargoForm(forms.ModelForm):
    class Meta:
        model = Cargo
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        date_widget_attrs = {
            'type': 'date',
            'class': 'form-control',
        }
