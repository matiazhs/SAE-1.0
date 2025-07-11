document.addEventListener('DOMContentLoaded', function() {
    // Función mejorada para manejar todos los casos
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
            
            // Casos especiales con múltiples elementos (como alergias)
            if (options.multiElements) {
                options.multiElements.forEach(element => {
                    const el = document.getElementById(element.id);
                    if (el) el.style.display = shouldShow ? element.display : 'none';
                });
            }
        }

        triggerRadios.forEach(radio => radio.addEventListener('change', toggle));
        toggle(); // Estado inicial
    }

    // ========== CONFIGURACIÓN DE TODOS LOS CAMPOS ========== //
    
    // --- Obra social (caso simple) ---
    setupConditionalField('obra_social', 'obra-social');
    
    // --- Internaciones (con limpieza de campos) ---
    setupConditionalField('int_comun', 'int_sal_comun', {
        clearFields: ['#id_cuantas_veces', '#id_causas_diag']
    });
    
    setupConditionalField('int_int', 'int_ter_int', {
        clearFields: ['#id_cuantas_veces_2', '#id_causas_diag_2']
    });

    setupConditionalField('recive_med', 'cual-med', {
        clearRadios: 'input[name="cual_med"]'
    });

    setupConditionalField('alg_op', 'preguntas', {
        clearRadios: 'input[name="cual_med"]'
    });

    
    // --- Alergias (caso complejo con múltiples elementos) ---
    setupConditionalField('aler_graves', 'rdas', {
        multiElements: [
            { id: 'rda_izq', display: 'block' },
            { id: 'rda_der', display: 'block' }
        ]
    });
    
    // --- Campos de discapacidad (con limpieza de radios) ---
    setupConditionalField('dis_auditiva', 'usa-audifono', {
        clearRadios: 'input[name="usa_audifono"]'
    });
    
    setupConditionalField('dis_visual', 'usa-lentes', {
        clearRadios: 'input[name="usa_lentes"]'
    });
    
    // ========== CASOS ESPECIALES (Checkboxes) ========== //
    
    // Función específica para checkboxes (alergias izquierda/derecha)
    function setupCheckboxToggle(checkboxName, suffix = '_confirma') {
        const checkboxes = document.querySelectorAll(`input[name="${checkboxName}"]`);
        
        checkboxes.forEach(checkbox => {
            checkbox.addEventListener('change', function() {
                const targetId = this.value + suffix;
                const targetDiv = document.getElementById(targetId);
                if (targetDiv) {
                    targetDiv.style.display = this.checked ? 'block' : 'none';
                }
            });
            
            // Inicializar estado si ya está checked
            if (checkbox.checked) {
                const targetId = checkbox.value + suffix;
                const targetDiv = document.getElementById(targetId);
                if (targetDiv) targetDiv.style.display = 'block';
            }
        });
    }
    
    // Configurar los checkboxes de alergias
    setupCheckboxToggle('alergias_izq');
    setupCheckboxToggle('alergias_der');
});