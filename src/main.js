const loginBtn = document.querySelector('#login-submit');
const username = document.getElementById('username');
const password = document.getElementById('password');
const usernameSpan = document.getElementById('username-label');
const passwordSpan = document.getElementById('password-label');

const menu = document.querySelector('#menu');
const smallNav = document.querySelector('.small-screen-nav-content');
const smallSearch = document.querySelector('#small-search');

menu.addEventListener('click', showMobileNav);


function loginAuthentication() {
    //Authentication code
}


function showMobileNav() {
    smallNav.classList.toggle('show-nav')
}

document.body.addEventListener('click', (e) => {
    if (smallNav.classList.contains('show-nav')) {
        if (e.target === menu || e.target === smallNav || e.target === smallSearch) {
            return
        } else {
            smallNav.classList.remove('show-nav')
        }
    } else {
        return
    }
})

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