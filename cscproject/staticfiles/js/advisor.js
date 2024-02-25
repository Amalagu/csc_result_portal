/* import { barChart, lineChart } from './studentChart.js'
import { onDetailsPopup } from './popup.js'
 */

/* DO NOT UNCOMMENT FROM HERE */
/* import { onImageUpload } from './image-upload.js'

onImageUpload('#profile-image', '#change-image-form input[type="file"]','#change-image-form input[type="submit"]') */
/* TO HERE!!! */


/* if (document.getElementById('full-student-details')) {onDetailsPopup('#full-student-details')}


const radioBtns = document.querySelectorAll('input[name="chartType"]')
const ctx = document.getElementById('bar-chart')
const ctx2 = document.getElementById('line-chart');

if (ctx) barChart(getData())

radioBtns.forEach(btn => btn.addEventListener('change', function() {

    if (btn.id === 'bar') {
        ctx.style.display = 'block'
        ctx2.style.display = 'none'

    } else if (btn.id === 'line') {
        ctx.style.display = 'none'
        ctx2.style.display = 'block'
        lineChart(getData())

    }
}))

function getData() {
    //API Call to be made here to get the data
    const data = [4.32, 3.55, 4.1, 4.43, 3.86]
    return  data
}

const studentSearchForm = document.querySelector('#student-search-form')
const studentSearch = document.querySelector('#student-search')

if (studentSearchForm) {
    studentSearchForm.addEventListener('submit', (e) => {
        e.preventDefault()
        if (studentSearch.value === '') return
    })
} */






import { barChart, lineChart } from './studentChart.js'
import { onDetailsPopup } from './popup.js'

/* import { onImageUpload } from './image-upload.js'

onImageUpload('#profile-image', '#change-image-form input[type="file"]','#change-image-form input[type="submit"]') */

if (document.getElementById('full-student-details')) {onDetailsPopup('#full-student-details')}


const radioBtns = document.querySelectorAll('input[name="chartType"]')
const ctx = document.getElementById('bar-chart')
const ctx2 = document.getElementById('line-chart');

if (ctx) barChart(getData())

radioBtns.forEach(btn => btn.addEventListener('change', function() {

    if (btn.id === 'bar') {
        ctx.style.display = 'block'
        ctx2.style.display = 'none'

    } else if (btn.id === 'line') {
        ctx.style.display = 'none'
        ctx2.style.display = 'block'
        lineChart(getData())

    }
}))

function getData() {
    //API Call to be made here to get the data
    const data = [4.32, 3.55, 4.1, 4.43, 3.86]
    return  data
}

const studentSearchForm = document.querySelector('#student-search-form')
const studentSearch = document.querySelector('#student-search')

if (studentSearchForm) {
    studentSearchForm.addEventListener('submit', (e) => {
        e.preventDefault()
        if (studentSearch.value === '') return
    })
}

















