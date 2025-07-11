document.addEventListener("DOMContentLoaded", function () {
    const poseeDniRadios = document.querySelectorAll('input[name="posee_dni"]');
    const dniExtraSection = document.getElementById("dni-extra");
    const dniArgentinoDetalle = document.getElementById("dni-argentino-detalle");

    const docExtranjeroRadios = document.querySelectorAll('input[name="doc_extranjero"]');
    const docDetalleSection = document.getElementById("doc-extranjero-detalle");

    const identidadRadios = document.querySelectorAll('input[name="identidad_genero"]');
    const otraIdentidadDiv = document.getElementById("otra-identidad");

    const lugarNacimientoRadios = document.querySelectorAll('input[name="lugar_nacimiento"]');
    const nacionalidadExteriorDiv = document.getElementById("extranjero-nacionalidad");

    const nacimientoArgentinaDiv = document.getElementById("nacimiento-argentina");
    const nacimientoArgentinaRadios = document.querySelectorAll('input[name="nac_argentina_opcion"]');
    const provinciaOtraDiv = document.getElementById("provincia-otra");
    const direccionBsAsDiv = document.getElementById("direccion-bsas");

    const tieneHermanosRadios = document.querySelectorAll('input[name="tiene_hermanos"]');
    const hermanosDetalleDiv = document.getElementById("hermanos-detalle");

    const tieneIdiomaHogarRadios = document.querySelectorAll('input[name="idioma_hogar"]');
    const lenguasDetalleDiv = document.getElementById("lenguas-detalle");

    const tieneHijosRadios = document.querySelectorAll('input[name="tiene_hijos"]');
    const asisteMaternalesSection = document.getElementById("as-maternales");

    function toggleDniExtra() {
        const seleccionado = document.querySelector('input[name="posee_dni"]:checked');
        if (!seleccionado) return;

        if (seleccionado.value === "no_posee") {
            dniExtraSection.style.display = "block";
            dniArgentinoDetalle.style.display = "none";
        } else {
            dniExtraSection.style.display = "none";
            dniArgentinoDetalle.style.display = "block";
            docDetalleSection.style.display = "none";
        }
    }

    function toggleDocExtranjero() {
        const seleccionado = document.querySelector('input[name="doc_extranjero"]:checked');
        docDetalleSection.style.display = (seleccionado && seleccionado.value === "si") ? "block" : "none";
    }

    function toggleOtraIdentidad() {
        const seleccion = document.querySelector('input[name="identidad_genero"]:checked');
        otraIdentidadDiv.style.display = (seleccion && seleccion.value === "otra") ? "block" : "none";
    }

    function toggleLugarNacimiento() {
        const seleccionado = document.querySelector('input[name="lugar_nacimiento"]:checked');
        if (!seleccionado) return;

        const esExtranjero = seleccionado.value === "extranjero";

        nacionalidadExteriorDiv.style.display = esExtranjero ? "block" : "none";
        nacimientoArgentinaDiv.style.display = esExtranjero ? "none" : "block";
        direccionBsAsDiv.style.display = "block";

        if (!esExtranjero) {
            toggleNacimientoArgentina();
        } else {
            provinciaOtraDiv.style.display = "none";
        }
    }

    function toggleNacimientoArgentina() {
        const seleccionado = document.querySelector('input[name="nac_argentina_opcion"]:checked');
        if (!seleccionado) {
            provinciaOtraDiv.style.display = "none";
            return;
        }

        provinciaOtraDiv.style.display = seleccionado.value === "otra" ? "block" : "none";
    }

    function toggleGrupoFamiliar() {
        const seleccionado = document.querySelector('input[name="tiene_hermanos"]:checked');
        hermanosDetalleDiv.style.display = (seleccionado && seleccionado.value === "si") ? "block" : "none";
    }

    function toggleLenguasDetalle() {
        const seleccionado = document.querySelector('input[name="idioma_hogar"]:checked');
        lenguasDetalleDiv.style.display = (seleccionado && seleccionado.value === "si") ? "block" : "none";
    }

    // Nueva función para mostrar/ocultar el bloque de asiste_maternales
    function toggleAsisteMaternales() {
        const seleccionado = document.querySelector('input[name="tiene_hijos"]:checked');
        if (seleccionado) {
            asisteMaternalesSection.style.display = (seleccionado.value === "si") ? "block" : "none";
        }
    }

    // Añadimos los eventos para las opciones de cada sección
    poseeDniRadios.forEach(r => r.addEventListener("change", toggleDniExtra));
    docExtranjeroRadios.forEach(r => r.addEventListener("change", toggleDocExtranjero));
    identidadRadios.forEach(r => r.addEventListener("change", toggleOtraIdentidad));
    lugarNacimientoRadios.forEach(r => r.addEventListener("change", toggleLugarNacimiento));
    nacimientoArgentinaRadios.forEach(r => r.addEventListener("change", toggleNacimientoArgentina));
    tieneHermanosRadios.forEach(r => r.addEventListener("change", toggleGrupoFamiliar));
    tieneIdiomaHogarRadios.forEach(r => r.addEventListener("change", toggleLenguasDetalle));
    tieneHijosRadios.forEach(r => r.addEventListener("change", toggleAsisteMaternales)); // Evento para mostrar/ocultar asiste_maternales

    function inicializarFormulario() {
        toggleDniExtra();
        toggleDocExtranjero();
        toggleOtraIdentidad();
        toggleGrupoFamiliar();
        toggleLugarNacimiento();
        toggleNacimientoArgentina();
        toggleLenguasDetalle();
        toggleAsisteMaternales(); // Llamamos a la función para inicializar correctamente asiste_maternales
    
        nacionalidadExteriorDiv.style.display = "none";
        nacimientoArgentinaDiv.style.display = "none";
        direccionBsAsDiv.style.display = "none";
        hermanosDetalleDiv.style.display = "none";
        lenguasDetalleDiv.style.display = "none";
        asisteMaternalesSection.style.display = "none"; // Aseguramos que esté oculto al inicio
    }

    inicializarFormulario();
});
