const fullDetailsBtns = document.querySelectorAll('.view-full-details')
const rightSideBox = document.querySelector('.container > .container-right')

fullDetailsBtns.forEach(btn => {
    btn.addEventListener('click', function() {
        if (window.getComputedStyle(rightSideBox).getPropertyValue('display') === 'none') {
            const courseDetails = document.querySelector('.view-details-small-screen')
            courseDetails.classList.add('show-details')

            const closeBtn = document.querySelector('.view-details-small-screen > button')
            closeBtn.addEventListener('click', function() {
                courseDetails.classList.remove('show-details')
            })

            const partToExclude = document.querySelector('.view-details-small-screen .course-desc > p')

            courseDetails.addEventListener('click', function(e) {
                if (e.target !== partToExclude) {
                    courseDetails.classList.remove('show-details')
                }
            })
        }
    })
})


