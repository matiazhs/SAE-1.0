$(document).ready(function () {
    var table = $('#tablaGrupos').DataTable({
        language: {
            url: '/static/json/es-ES.json'
        },
        responsive: true
    });


    $('#buscadorPersonalizado').on('keyup', function () {
        table.search(this.value).draw();
    });

    $('#btnLimpiarBusqueda').on('click', function () {
        $('#buscadorPersonalizado').val('');
        table.search('').columns().search('').draw();
    });
});