// Clean Blog JavaScript

document.addEventListener('DOMContentLoaded', function() {
    // Navbar scroll effect
    const mainNav = document.getElementById('mainNav');
    
    if (mainNav) {
        window.addEventListener('scroll', function() {
            if (window.scrollY > 100) {
                mainNav.classList.add('scrolled');
            } else {
                mainNav.classList.remove('scrolled');
            }
        });
        
        // Trigger on load in case page is already scrolled
        if (window.scrollY > 100) {
            mainNav.classList.add('scrolled');
        }
    }
    
    // Mobile menu toggle
    const navToggle = document.querySelector('.nav-toggle');
    const navLinks = document.querySelector('.nav-links');
    
    if (navToggle && navLinks) {
        navToggle.addEventListener('click', function() {
            navLinks.classList.toggle('active');
        });
    }
    
    // Form validation (basic)
    const contactForm = document.querySelector('.contact-form form');
    
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            const name = document.getElementById('name');
            const email = document.getElementById('email');
            const message = document.getElementById('message');
            
            let isValid = true;
            
            if (name && name.value.trim() === '') {
                isValid = false;
                name.style.borderColor = '#dc3545';
            }
            
            if (email && !isValidEmail(email.value)) {
                isValid = false;
                email.style.borderColor = '#dc3545';
            }
            
            if (message && message.value.trim() === '') {
                isValid = false;
                message.style.borderColor = '#dc3545';
            }
            
            if (!isValid) {
                e.preventDefault();
            }
        });
    }
    
    function isValidEmail(email) {
        const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return re.test(email);
    }
    
    // Smooth scroll for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });
});
