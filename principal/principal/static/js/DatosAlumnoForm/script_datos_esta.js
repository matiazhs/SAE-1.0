document.addEventListener('DOMContentLoaded', function() {
    // --- Manejo de selección de país (sector_pp_2) ---
    const paisRadios = document.querySelectorAll('input[name="sector_pp_2"]');
    const paisDet1 = document.getElementById('pais-det-1');
    const paisDet2 = document.getElementById('pais-det-2');

    function togglePaisFields() {
        const selectedValue = document.querySelector('input[name="sector_pp_2"]:checked')?.value;
        
        paisDet1.style.display = 'none';
        paisDet2.style.display = 'none';
        
        if (selectedValue === 'otrop') {
            paisDet1.style.display = 'block';
        } else if (selectedValue === 'argentina') {
            paisDet2.style.display = 'block';
        }
    }

    paisRadios.forEach(radio => {
        radio.addEventListener('change', togglePaisFields);
    });

    // --- Manejo de selección de provincia (select_prov) ---
    const provRadios = document.querySelectorAll('input[name="select_prov"]');
    const provDet = document.getElementById('prov-det');

    function toggleProvFields() {
        const selectedValue = document.querySelector('input[name="select_prov"]:checked')?.value;
        
        if (selectedValue === 'otrap2') {
            provDet.style.display = 'block';
        } else {
            provDet.style.display = 'none';
            // Opcional: Limpiar el campo cuando se oculta
            const provField = document.querySelector('[name="prov_4"]');
            if (provField) provField.value = "";
        }
    }

    provRadios.forEach(radio => {
        radio.addEventListener('change', toggleProvFields);
    });

    // --- Inicializar ambos conjuntos de campos ---
    togglePaisFields();
    toggleProvFields();
});