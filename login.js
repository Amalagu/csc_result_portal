const loginBtn = document.querySelector('#login-submit');
const username = document.getElementById('username');
const password = document.getElementById('password');
const usernameSpan = document.getElementById('username-label');
const passwordSpan = document.getElementById('password-label');


function loginAuthentication() {
    //Authentication code
}

loginBtn.addEventListener('click', (e)=>{
    e.preventDefault();
    if (username.value === "") {
        usernameSpan.hidden = false;
        username.style.border = "1px solid var(--danger)";
    } else {
        usernameSpan.hidden = true;
        username.style.border = "1px solid var(--body-200)";
    }
    
    if (password.value === "") {
        passwordSpan.hidden = false;
        password.style.border = "1px solid var(--danger)";

    } else {
        passwordSpan.hidden = true;
        password.style.border = "1px solid var(--body-200)";
    }

    if (username.value !== "" && password.value !=="") {
        usernameSpan.hidden = true;
        passwordSpan.hidden = true;
        username.style.border = "1px solid var(--body-200)";
        password.style.border = "1px solid var(--body-200)";

        loginAuthentication();
    }
})
