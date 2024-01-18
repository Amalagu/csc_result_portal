export function logoComponent(element) {
    const div = document.getElementById(element)
    div.classList = 'flex items-center gap-1'
    div.innerHTML = `
        <img src="{% static 'img/logo.svg' %}" alt="logo" width="38">
        <div>
            <p class="text-[.75rem] text-body-600 font-semibold">
                Department of Computer Science
            </p>
            <p class="text-[.65rem] text-body-400 font-light">
                Federal University of Technology, Owerri
            </p>
        </div>
     `
}
