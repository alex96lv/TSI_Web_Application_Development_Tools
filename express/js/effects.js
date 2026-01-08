// Effect 1: Smooth appearance of sections on page load
window.addEventListener('load', function() {
    const sections = document.querySelectorAll('.w3-container');
    sections.forEach((section, index) => {
        section.style.opacity = '0';
        section.style.transform = 'translateY(30px)';
        setTimeout(() => {
            section.style.transition = 'all 0.8s ease';
            section.style.opacity = '1';
            section.style.transform = 'translateY(0)';
        }, index * 200);
    });
});

// Effect 2: BRIGHT navbar color change on scroll
window.addEventListener('scroll', function() {
    const navbar = document.querySelector('.w3-bar');
    if (window.scrollY > 100) {
        navbar.style.backgroundColor = '#e74c3c';
        navbar.style.boxShadow = '0 4px 20px rgba(231, 76, 60, 0.4)';
        navbar.style.transition = 'all 0.5s ease';
    } else {
        navbar.style.backgroundColor = 'black';
        navbar.style.boxShadow = 'none';
    }
});

// Effect 3: NOTICEABLE button animation on click
document.addEventListener('click', function(e) {
    if (e.target.classList.contains('w3-button')) {
        // Create ripple effect
        e.target.style.position = 'relative';
        e.target.style.overflow = 'hidden';
        
        const ripple = document.createElement('span');
        ripple.style.position = 'absolute';
        ripple.style.borderRadius = '50%';
        ripple.style.background = 'rgba(255,255,255,0.6)';
        ripple.style.transform = 'scale(0)';
        ripple.style.animation = 'ripple 0.6s linear';
        ripple.style.left = '50%';
        ripple.style.top = '50%';
        ripple.style.width = '100px';
        ripple.style.height = '100px';
        ripple.style.marginLeft = '-50px';
        ripple.style.marginTop = '-50px';
        
        e.target.appendChild(ripple);
        
        setTimeout(() => {
            ripple.remove();
        }, 600);
    }
});

// Effect 4: Image color change on hover
document.addEventListener('DOMContentLoaded', function() {
    const images = document.querySelectorAll('img');
    images.forEach(img => {
        img.addEventListener('mouseenter', function() {
            this.style.filter = 'sepia(100%) hue-rotate(120deg) saturate(100%)';
            this.style.transition = 'filter 0.3s ease';
        });
        
        img.addEventListener('mouseleave', function() {
            this.style.filter = 'none';
        });
    });
});