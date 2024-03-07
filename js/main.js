// JavaScript
// Replace your existing JavaScript code with this

document.addEventListener('DOMContentLoaded', function () {
    const menuToggle = document.querySelector('.menu-toggle');
    const navLinks = document.querySelector('.nav-links');

    menuToggle.addEventListener('click', function () {
        navLinks.classList.toggle('active');
    });

    const navLinksA = document.querySelectorAll('.nav-links ul li a');

    navLinksA.forEach(link => {
        link.addEventListener('click', function (e) {
            e.preventDefault();
            navLinks.classList.remove('active');

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

let lastScrollTop = 0;
const header = document.querySelector('header');

window.addEventListener('scroll', function() {
    let scrollTop = window.pageYOffset || document.documentElement.scrollTop;

    if (scrollTop > lastScrollTop) {
        // Scroll down
        header.style.transition = 'top 0.3s';
        header.style.top = '-80px'; // Hide the header
    } else {
        // Scroll up
        header.style.transition = 'top 0.3s';
        header.style.top = '0'; // Show the header
    }

    lastScrollTop = scrollTop <= 0 ? 0 : scrollTop; // For Mobile or negative scrolling
}, false);