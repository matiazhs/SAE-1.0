document.addEventListener('DOMContentLoaded', function () {
    const formaIngreso = document.getElementById('formaIngreso');
    const resolucionContainer = document.getElementById('resolucionContainer');

    function toggleResolucionField() {
        const selected = formaIngreso.options[formaIngreso.selectedIndex].text.toLowerCase();
        if (selected.includes('disposicion')) {
            resolucionContainer.style.display = 'block';
        } else {
            resolucionContainer.style.display = 'none';
        }
    }

    formaIngreso.addEventListener('change', toggleResolucionField);

    // Ejecutar al cargar la página por si ya está seleccionada "Disposición"
    toggleResolucionField();
});