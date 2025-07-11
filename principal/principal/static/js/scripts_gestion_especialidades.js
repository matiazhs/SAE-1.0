$(document).ready(function () {
    var table = $('#tablaEspecialidades').DataTable({
        language: {
            url: '/static/json/es-ES.json'
        },
        responsive: true,
        //searching: false
    });

    $('#buscadorPersonalizado').on('keyup', function () {
        table.search(this.value).draw();
    });

    $('#btnLimpiarBusqueda').on('click', function () {
        $('#buscadorPersonalizado').val('');
        table.search('').columns().search('').draw();
    });
});