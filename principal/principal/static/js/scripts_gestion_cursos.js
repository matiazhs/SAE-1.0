$(document).ready(function () {
    // Inicializar DataTable
    var table = $('#tablaCursos').DataTable({
        language: {
            url: '/static/json/es-ES.json'
        },
        responsive: true
    });

    // Filtro por nombre
    $('#filtroNombre').on('change', function () {
        table.column(0).search(this.value).draw();
    });

    // Filtro por especialidad
    $('#filtroEspecialidad').on('change', function () {
        table.column(1).search(this.value).draw();
    });

    // Buscador personalizado
    $('#buscadorPersonalizado').on('keyup', function () {
        table.search(this.value).draw();
    });

    // Limpiar búsqueda
    $('#btnLimpiarBusqueda').on('click', function () {
        $('#buscadorPersonalizado').val('');
        $('#filtroNombre, #filtroEspecialidad').val('');
        table.search('').columns().search('').draw();
    });
});