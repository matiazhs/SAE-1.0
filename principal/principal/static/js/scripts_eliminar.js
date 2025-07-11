document.getElementById('confirmCheck').addEventListener('change', function () {
    document.getElementById('submitBtn').disabled = !this.checked;
});

document.getElementById('submitBtn').addEventListener('click', function (e) {
    if (!confirm('¿ESTÁ ABSOLUTAMENTE SEGURO?')) {
        e.preventDefault();
    }
});