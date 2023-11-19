const menu = document.querySelector('#menu');
const smallNav = document.querySelector('.small-screen-nav-content');
const smallSearch = document.querySelector('#small-search');


document.addEventListener('DOMContentLoaded', function() {
  hideOverlay();
});

window.addEventListener('beforeunload', function() {
  showOverlay();
});

window.addEventListener('load', function() {
  hideOverlay();
});

function showOverlay() {
  const overlay = document.getElementById('overlay');
  overlay.style.display = 'flex';
}

function hideOverlay() {
  const overlay = document.getElementById('overlay');
  overlay.style.display = 'none';
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

menu.addEventListener('click', showMobileNav);

