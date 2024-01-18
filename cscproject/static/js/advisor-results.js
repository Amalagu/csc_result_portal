const form = document.querySelector('#result-options-form')
const session = document.querySelector('#session')
const semester = document.querySelector('#semester')
const course = document.querySelector('#course')
const submitBtn = document.querySelector('#result-options-form button[type="submit"]')


function adjustFields() {
    if (session.value ==="" || semester.value ==="" || course.value ==="") {
        submitBtn.disabled = true
    } else {
        submitBtn.disabled = false
    }

    if (session.value !=="" && session.value !=='all') {
        semester.disabled = false
    }

    if (semester.value !=="") {
        course.disabled = false
    } else {
        course.disabled = true
    }
}

function viewResults() {
   console.log('View Results')
}


if (document.querySelector('#result-options-form')) {
    form.addEventListener('change', adjustFields)
    submitBtn.addEventListener('click', viewResults)
}

