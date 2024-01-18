export function toggleOverlay(element) {
    window.addEventListener('load', function() {
        const overlay = document.getElementById(element)
        setTimeout(() => {
            overlay.style.display = 'none'
        }, 500);
    })
}


