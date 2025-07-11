$(document).ready(function () {
    $('#tabla-tipos-cargo').DataTable({
        language: {
            url: '/static/json/es-ES.json'
        },
        columnDefs: [
            {
                targets: -1,       // Última columna (la de acciones)
                width: '90px',     // Ajustás el ancho a lo necesario
                orderable: false,  // Evitás que sea ordenable
                className: 'text-center' // (opcional) centrás el contenido
            }
        ]
    });
});
