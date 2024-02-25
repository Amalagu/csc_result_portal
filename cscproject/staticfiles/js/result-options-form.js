
document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('result-options-form');
    const submitButton = document.getElementById('submit-button');

    form.addEventListener('submit', function (event) {
        event.preventDefault();
        const session = document.getElementById('session').value;
        const semester = document.getElementById('semester').value.toString();
        const course = document.getElementById('course').value;
        const url = `{% url 'single_course_result' session_id=${session} semester_id=${semester} course_id=${course} %}`
        //const url = `/results/advisor/single/${session}/${semester}/${course}'`;
        //const url = `/results/advisor/single?session_id='${session}'&semester_id='${semester}'&course_id='${course}'`;
        
        //http://127.0.0.1:8000/results/advisor/semester?session_id=${session}&semester_id=${semester}&course_id=${course}/
        form.action = url;
        form.submit();
    });
});
