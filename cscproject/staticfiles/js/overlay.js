export function overlay(element) {
    const overlay = document.getElementById(element)
    overlay.innerHTML = `
        <img src="../../assets/images/logo.svg" alt="">
        <div class="spinner"> </div>
    `
}




/* export function overlay(element) {
    const overlay = document.getElementById(element);
    logoUrl = overlay.getAttribute('data-logo-url');
    logoUrl = "{% static 'img/logo.svg' %}"
    overlay.innerHTML = `
        <img src=${logoUrl} alt="">
        <div class="spinner"> </div>
    `;
} */
