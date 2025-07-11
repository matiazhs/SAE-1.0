$(document).ready(function () {
    var table = $('#tablaAlumnos').DataTable({
        language: {
            url: '/static/json/es-ES.json'
        },
        responsive: true,
        dom: '<"top"i>rt<"bottom"lp><"clear">', // Elimina el buscador por defecto
        pageLength: 10
    });

    // Filtro por Curso
    $('#filtroCurso').on('change', function () {
        var curso = $(this).val();
        table.column(5).search(curso).draw(); // Índice 5 para la columna Especialidad
    });

    // Filtro por Especialidad
    $('#filtroEspecialidad').on('change', function () {
        var especialidad = $(this).val();
        table.column(6).search(especialidad).draw(); // Índice 6 para la columna especialidad
    });

    // Buscador personalizado (busca en todas las columnas)
    $('#buscadorPersonalizado').keyup(function () {
        table.search($(this).val()).draw();
    });

    // Botón para limpiar búsqueda
    $('#btnLimpiarBusqueda').click(function () {
        $('#buscadorPersonalizado').val('');
        table.search('').draw();
    });
});