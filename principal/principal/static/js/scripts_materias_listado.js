document.addEventListener("DOMContentLoaded", function () {
    const tablaElement = document.getElementById("tablaMaterias");
    if (!tablaElement) return;

    const filas = tablaElement.querySelectorAll("tbody tr");

    const cursos = new Set();
    const grupos = new Set();
    const especialidades = new Set();
    const docentes = new Set();

    function agregarValores(set, texto, separador) {
        texto.split(separador).forEach(valor => {
            const v = valor.trim();
            if (v) set.add(v);
        });
    }

    filas.forEach(fila => {
        const celdas = fila.querySelectorAll("td");
        if (celdas.length === 0) return;

        // Curso
        cursos.add(celdas[1].textContent.trim());

        // Grupos
        agregarValores(grupos, celdas[2].innerHTML, "<br>");

        // Especialidades
        agregarValores(especialidades, celdas[3].textContent, ",");

        // Docentes
        celdas[4].innerHTML.split("<br>").forEach(docente => {
            const d = docente.trim();
            if (d && !d.toLowerCase().includes("sin docente")) docentes.add(d);
        });
    });

    function llenarSelect(idSelect, valores) {
        const select = document.getElementById(idSelect);
        if (!select) return;

        select.innerHTML = `<option value="">Todos</option>`;
        Array.from(valores).sort().forEach(valor => {
            select.innerHTML += `<option value="${valor}">${valor}</option>`;
        });
    }

    llenarSelect("filtroCurso", cursos);
    llenarSelect("filtroGrupo", grupos);
    llenarSelect("filtroEspecialidad", especialidades);
    llenarSelect("filtroDocente", docentes);
});


$(document).ready(function () {
    const tabla = $('#tablaMaterias').DataTable({
        paging: true,
        language: {
            url: '/static/json/es-ES.json'
        }
    });

    // Buscador general
    $('#buscadorPersonalizado').on('keyup', function () {
        tabla.search(this.value).draw();
        toggleBotonLimpiar();
    });

    const inputBusqueda = document.getElementById("buscadorPersonalizado");
    const botonLimpiar = document.getElementById("btnLimpiarBusqueda");

    function toggleBotonLimpiar() {
        if (inputBusqueda.value.trim() !== "") {
            botonLimpiar.style.display = "inline-block";
        } else {
            botonLimpiar.style.display = "none";
        }
    }
    toggleBotonLimpiar();

    // Filtros acumulativos
    const filtros = {
        grupo: '',
        especialidad: '',
        docente: ''
    };

    function aplicarFiltros() {
        $.fn.dataTable.ext.search = [
            function (settings, data) {
                const grupo = data[2]?.toLowerCase() || '';
                const especialidad = data[3]?.toLowerCase() || '';
                const docente = data[4]?.toLowerCase() || '';

                return (!filtros.grupo || grupo.includes(filtros.grupo)) &&
                    (!filtros.especialidad || especialidad.includes(filtros.especialidad)) &&
                    (!filtros.docente || docente.includes(filtros.docente));
            }
        ];
        tabla.draw();
    }

    $('#filtroCurso').on('change', function () {
        const val = $(this).val();
        tabla.column(1).search(val ? '^' + val + '$' : '', true, false).draw();
    });

    $('#filtroGrupo').on('change', function () {
        filtros.grupo = this.value.toLowerCase();
        aplicarFiltros();
    });

    $('#filtroEspecialidad').on('change', function () {
        filtros.especialidad = this.value.toLowerCase();
        aplicarFiltros();
    });

    $('#filtroDocente').on('change', function () {
        filtros.docente = this.value.toLowerCase();
        aplicarFiltros();
    });

    botonLimpiar.addEventListener("click", function () {
        inputBusqueda.value = "";

        // Limpiar búsqueda general
        tabla.search("");

        // Resetear filtros acumulativos
        filtros.grupo = '';
        filtros.especialidad = '';
        filtros.docente = '';

        // Limpiar selects de filtros
        $('#filtroCurso').val('');
        $('#filtroGrupo').val('');
        $('#filtroEspecialidad').val('');
        $('#filtroDocente').val('');

        // Quitar filtros personalizados de DataTables
        $.fn.dataTable.ext.search = [];

        // Redibujar tabla con todo limpio
        tabla.draw();

        toggleBotonLimpiar();
        inputBusqueda.focus();
    });
});

