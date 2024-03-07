document.addEventListener('DOMContentLoaded', function () {
    const navLinks = document.querySelectorAll('nav ul li a');

    navLinks.forEach(link => {
        link.addEventListener('click', function (e) {
            e.preventDefault();

            const targetId = this.getAttribute('href').substring(1);
            const targetSection = document.getElementById(targetId);
            const navbarHeight = document.querySelector('nav').offsetHeight;
            const targetOffset = targetSection.offsetTop - navbarHeight;
            const scrollPosition = targetOffset - window.innerHeight / 2 + targetSection.offsetHeight / 2;

            window.scrollTo({
                top: scrollPosition,
                behavior: 'smooth'
            });
        });
    });
});