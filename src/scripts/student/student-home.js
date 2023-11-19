const toggleBtn = document.querySelector('#toggle-btn')

toggleBtn.addEventListener('click', function() {
    const details = document.querySelector('.container-right')
    const semesterCourses = document.querySelector('.container-left')

    if (!details.classList.contains('show-container-right')) {
        details.classList.add('show-container-right')
        semesterCourses.classList.add('hide-container-left')
        toggleBtn.textContent = 'Hide Personal Details'
        toggleBtn.className = 'btn-small-accent'
    } else {
        details.classList.remove('show-container-right')
        semesterCourses.classList.remove('hide-container-left')
        toggleBtn.textContent = 'Show Personal Details'
        toggleBtn.className = 'btn-small-primary'
    }
})