const themeSwitch = document.querySelector('.theme-switch');

// Al cargar la página, verifica si hay una preferencia almacenada y aplica el tema
document.addEventListener('DOMContentLoaded', () => {
    const storedTheme = localStorage.getItem('theme');

    if (storedTheme) {
        document.documentElement.setAttribute('data-theme', storedTheme);
    }
});

themeSwitch.addEventListener('click', toggleTheme);

function toggleTheme() {
    const currentTheme = document.documentElement.getAttribute('data-theme');
    
    const newTheme = currentTheme === 'light' ? 'dark' : 'light';
    
    document.documentElement.setAttribute('data-theme', newTheme);

    // Almacena la preferencia del tema en el almacenamiento local
    localStorage.setItem('theme', newTheme);

    const moonIcon = document.querySelector('.fa-moon');
    const sunIcon = document.querySelector('.fa-sun');

    if (newTheme === 'dark') {
        moonIcon.style.display = 'none';
        sunIcon.style.display = 'inline-block';
    } else {
        moonIcon.style.display = 'inline-block';
        sunIcon.style.display = 'none';
    }
}


function toggleProyectos() {
    const proyectosExtra = document.querySelector('.proyectos-extra');
    proyectosExtra.classList.toggle('show-more');

    const toggleMoreButton = document.querySelector('.toggle-more');
    
    if (proyectosExtra.classList.contains('show-more')) {
        toggleMoreButton.textContent = 'Ver menos 👆';
    } else {
        toggleMoreButton.textContent = 'Ver más 👇';
    }
}
