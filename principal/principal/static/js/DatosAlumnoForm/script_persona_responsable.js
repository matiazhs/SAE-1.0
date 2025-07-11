document.addEventListener('DOMContentLoaded', function () {
    function setupConditionalField(triggerName, config = {}) {
        const triggerRadios = document.querySelectorAll(`input[name="${triggerName}"]`);

        if (!triggerRadios.length) {
            console.warn(`No se encontraron radios para: ${triggerName}`);
            return;
        }

        function toggle() {
            const selected = document.querySelector(`input[name="${triggerName}"]:checked`);
            const selectedValue = selected ? selected.value : null;

            // Ocultar todos los divs del config
            Object.values(config).forEach(cfg => {
                const targetDiv = document.getElementById(cfg.targetId);
                if (targetDiv) targetDiv.style.display = 'none';

                // Limpiar campos si corresponde
                if (cfg.clearFields) {
                    cfg.clearFields.forEach(selector => {
                        const field = document.querySelector(selector);
                        if (field) field.value = "";
                    });
                }

                if (cfg.clearRadios) {
                    document.querySelectorAll(cfg.clearRadios).forEach(radio => {
                        radio.checked = false;
                    });
                }
            });

            // Mostrar el div que corresponde al valor seleccionado
            if (selectedValue && config[selectedValue]) {
                const cfg = config[selectedValue];
                const targetDiv = document.getElementById(cfg.targetId);
                if (targetDiv) targetDiv.style.display = 'block';
            }
        }

        triggerRadios.forEach(radio => radio.addEventListener('change', toggle));
        toggle(); // Estado inicial
    }

    // ========= CONFIGURACIÓN ========= //

    setupConditionalField('dni_adul_1', {
        'sit': {
            targetId: 'dni_opt_adul_1',
            //clearFields: ['input[name="ndoc_adul_1"]'],
        },
        'sin': {
            targetId: 'dni_opt_adul_1',
            //clearFields: ['input[name="ndoc_adul_1"]'],
        },
        'not': {
            targetId: 'dni_opt_2_adul_1',
            //clearFields: ['input[name="ndoc_adul_1"]'],
        }
    });


    setupConditionalField('dni_adul_2', {
        'sit': {
            targetId: 'dni_opt_adul_2',
            //clearFields: ['input[name="ndoc_adul_2"]'],
        },
        'sin': {
            targetId: 'dni_opt_adul_2',
            //clearFields: ['input[name="ndoc_adul_2"]'],
        },
        'not': {
            targetId: 'dni_opt_2_adul_2',
            //clearFields: ['input[name="ndoc_adul_2"]'],
        }
    });


    setupConditionalField('doc_extra1', {
        'si': {
            targetId: 'dni_opt_2_adul_11',
            //clearFields: ['input[name="ndoc_adul_2"]'],
        }
    });

    setupConditionalField('doc_extra2', {
        'si': {
            targetId: 'dni_opt_2_adul_22',
            //clearFields: ['input[name="ndoc_adul_2"]'],
        }
    });

    setupConditionalField('asis_esta_edu_adul_1', {
        'si': {
            targetId: 'comp_niv_op_1',
            //clearFields: ['input[name="ndoc_adul_2"]'],
        }
    });

    setupConditionalField('asis_esta_edu_adul_2', {
        'si': {
            targetId: 'comp_niv_op_2',
            //clearFields: ['input[name="ndoc_adul_2"]'],
        }
    });

    setupConditionalField('vive_est_1', {
        'no': {
            targetId: 'final_1',
            //clearFields: ['input[name="ndoc_adul_2"]'],
        }
    });

    setupConditionalField('vive_est_2', {
        'no': {
            targetId: 'final_2',
            //clearFields: ['input[name="ndoc_adul_2"]'],
        }
    });


});


// Otro ejemplo (completalo con los tuyos)
    // setupConditionalField('xxx', 'xxx2', {
    //     showIf: ['si'],
    //     clearFields: ['input[name="otro"]'],
    //     clearRadios: 'input[name="otro_radio"]'
    // });