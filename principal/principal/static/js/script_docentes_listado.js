function crearCeldaSituacion(situacion) {
    situacion = situacion || 'Desconocido';
    //console.log('Situación recibida:', '"' + situacion + '"');

    const celdaSituacion = $('<td>').addClass('celda-situacion').attr('data-situacion', situacion);

    const contenidoSituacion = $('<div>').addClass('contenido-situacion');
    const spanSituacion = $('<span>').text(situacion);
    const colorBox = $('<div>').addClass('color-box');

    switch (situacion.trim().toUpperCase()) {
        case 'SUPLENTE':
            colorBox.css('background-color', 'green');
            break;
        case 'TITULAR':
            colorBox.css('background-color', 'blue');
            break;
        case 'PROVISIONAL':
            colorBox.css('background-color', 'red');
            break;
        case 'TITULAR INT.':
            colorBox.css('background-color', 'yellow');
            break;
        default:
            colorBox.css('background-color', 'red');
    }

    contenidoSituacion.append(spanSituacion).append(colorBox);
    celdaSituacion.append(contenidoSituacion);

    return celdaSituacion;
}

$(document).ready(function () {
    // Activar DataTables con idioma español
    var tabla = $('#tablaDocentes').DataTable({
        language: {
            url: '/static/json/es-ES.json'
        },
        responsive: true
    });

    // Limpiar búsqueda personalizada
    $('#btnLimpiarBusqueda').click(function () {
        $('#buscadorPersonalizado').val('');
        $('#tablaDocentes').DataTable().search('').draw();
    });

    // Buscador personalizado
    $('#buscadorPersonalizado').on('input', function () {
        $('#tablaDocentes').DataTable().search($(this).val()).draw();
    });

    // Evento de click en botón "ver materias"
    $('.ver-materias-btn').click(function () {
        const docenteId = $(this).data('docente-id');
        const tbody = $('#materiasDocenteBody');
        tbody.empty();

        $.ajax({
            url: docenteId + '/materias/',
            method: 'GET',
            success: function (data) {
                data.forEach(function (asignacion) {
                    const row = $('<tr>');
                    row.append($('<td>').text(asignacion.materia.nombre));
                    row.append($('<td>').text(asignacion.materia.tipo));
                    row.append($('<td>').text(asignacion.materia.pid));
                    row.append($('<td>').text(asignacion.materia.cupof));
                    row.append($('<td>').text(asignacion.materia.fecha_toma_posesion));

                    const formaIngreso = asignacion.materia.forma_ingreso;
                    const numeroDispo = asignacion.materia.numero_dispo;

                    let textoFormaIngreso = formaIngreso;
                    if (formaIngreso === 'DIS' && numeroDispo) {
                        textoFormaIngreso += ' Nº ' + numeroDispo;
                    }

                    row.append($('<td>').text(textoFormaIngreso));

                    //row.append($('<td>').text(asignacion.materia.forma_ingreso + numeroDispo));
                    //row.append($('<td>').text(asignacion.materia.situacion_revista));
                    row.append(crearCeldaSituacion(asignacion.situacion_revista));
                    row.append($('<td>').text(asignacion.materia.secuencia));
                    row.append($('<td>').text(asignacion.materia.especialidad.nombre));
                    row.append($('<td>').text(asignacion.materia.curso.nombre));
                    row.append($('<td>').text(asignacion.grupo.nombre));
                    row.append($('<td>').text(asignacion.materia.aula ? asignacion.materia.aula.nombre : 'Sin aula asignada'));
                    row.append($('<td>').text(asignacion.materia.dias_semana));
                    row.append($('<td>').text(asignacion.materia.horario_inicio + ' - ' + asignacion.materia.horario_fin));

                    tbody.append(row);
                });
            },
            error: function () {
                alert('Error al cargar las materias del docente');
            }
        });
    });
});