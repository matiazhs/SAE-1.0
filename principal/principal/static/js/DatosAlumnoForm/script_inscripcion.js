document.addEventListener('DOMContentLoaded', function() {
    // Función reutilizable (la misma del script original)
    function setupConditionalField(triggerName, targetId, options = {}) {
        const triggerRadios = document.querySelectorAll(`input[name="${triggerName}"]`);
        const targetDiv = document.getElementById(targetId);
        
        if (!triggerRadios.length || !targetDiv) {
            console.warn(`Elementos no encontrados para: ${triggerName} -> ${targetId}`);
            return;
        }

        function toggle() {
            const selected = document.querySelector(`input[name="${triggerName}"]:checked`);
            const shouldShow = selected && selected.value === 'si';
            
            // Mostrar/ocultar el div principal
            targetDiv.style.display = shouldShow ? 'block' : 'none';
            
            // Limpiar campos de texto si se especificó
            if (options.clearFields && !shouldShow) {
                options.clearFields.forEach(selector => {
                    const field = document.querySelector(selector);
                    if (field) field.value = "";
                });
            }
            
            // Limpiar radios si se especificó
            if (options.clearRadios && !shouldShow) {
                document.querySelectorAll(options.clearRadios).forEach(radio => {
                    radio.checked = false;
                });
            }
        }

        triggerRadios.forEach(radio => radio.addEventListener('change', toggle));
        toggle(); // Estado inicial
    }

    // ========== CONFIGURACIÓN DE CAMPOS ========== //
    
    // --- Inclusión (con limpieza de radios anidados) ---
    setupConditionalField('cursa_p_inclu', 'inclu_s_n', {
        clearRadios: 'input[name="esc_cursa"], input[name="tiene_acomp"]'
    });
    
    // [Aquí puedes agregar más configuraciones si necesitas otros campos condicionales]
});