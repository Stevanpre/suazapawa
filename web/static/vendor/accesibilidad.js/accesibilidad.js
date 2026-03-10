document.addEventListener("DOMContentLoaded", function() {
    const buttonLabels = {
        "Readable Font": "Fuente Legible",
        "Underline Links": "Subrayar Enlaces",
        "Highlight Title": "Resaltar Título",
        "Monochrome": "Monocromo",
        "Low Saturation": "Baja Saturación",
        "High Saturation": "Alta Saturación",
        "High Contrast": "Alto Contraste",
        "Light Contrast": "Bajo Contraste",
        "Big Cursor": "Cursor Grande",
        "Stop Animations": "Detener Animaciones",
        "Highlight Links": "Resaltar Enlaces",
    };

    document.querySelectorAll('.asw-btn').forEach(button => {
        const key = button.querySelector('.material-icons').nextSibling.nodeValue.trim();
        if (buttonLabels[key]) {
            button.querySelector('.material-icons').nextSibling.nodeValue = buttonLabels[key];
        }
    });
});