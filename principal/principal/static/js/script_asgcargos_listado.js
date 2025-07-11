$(document).ready(function () {
    // Activar DataTables con idioma español
    var tabla = $('#tablaCargos').DataTable({
        language: {
            url: '/static/json/es-ES.json'
        },
        responsive: true
    });

    // Limpiar búsqueda personalizada y filtro por cargo
    $('#btnLimpiarBusqueda').click(function () {
        $('#buscadorPersonalizado').val('');
        $('#filtroCargo').val(''); // Limpiar select cargo
        tabla.search('').columns().search('').draw();
    });

    // Buscador personalizado
    $('#buscadorPersonalizado').on('input', function () {
        tabla.search($(this).val()).draw();
    });

    // Filtro por cargo
    $('#filtroCargo').on('change', function () {
        var valor = $(this).val();
        if (valor) {
            tabla.column(6).search('^' + valor + '$', true, false).draw(); // columna 6 = Cargo
        } else {
            tabla.column(6).search('').draw();
        }
    });
});
