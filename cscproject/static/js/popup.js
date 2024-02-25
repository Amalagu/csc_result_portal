export function onNavPopup(nav) {
  const popup = document.querySelector(nav);

  function openPopup() {
    popup.style.display = 'flex';
  }

  function closePopup() {
    popup.style.display = 'none';
  }

  document.addEventListener('DOMContentLoaded', () => {
    if (window.innerWidth >= 1280) {
      openPopup()
      return
    }
  })

  window.addEventListener('resize', () => {
    if (window.innerWidth >= 1280) {
      openPopup();
    } else {
      closePopup();
    }
  })
}

export function onSidebarPopup(details) {
  const sidebar = document.querySelector(details)
  
  function openPopup() {
    sidebar.style.display = 'flex';
  }

  function closePopup() {
    sidebar.style.display = 'none';
  }

  document.addEventListener('DOMContentLoaded', () => {
    if (window.innerWidth >= 1024) {
      openPopup()
      return
    } else {
      closePopup()
      return
    }
  })

  window.addEventListener('resize', () => {
    if (window.innerWidth >= 1024) {
      openPopup();
      return
    } else {
      closePopup();
      return
    }
  })
}

export function onDetailsPopup(details) {
  const sidebar = document.querySelector(details)
  
  function openPopup() {
    sidebar.style.display = 'block';
  }

  function closePopup() {
    sidebar.style.display = 'none';
  }

  document.addEventListener('DOMContentLoaded', () => {
    if (window.innerWidth >= 1024) {
      openPopup()
      return
    } else {
      closePopup()
      return
    }
  })

  window.addEventListener('resize', () => {
    if (window.innerWidth >= 1024) {
      openPopup();
      return
    } else {
      closePopup();
      return
    }
  })
}

