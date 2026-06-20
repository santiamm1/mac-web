/**
 * Miguel Cordini - Soluciones e Insumos Agropecuarios
 * Main JavaScript Interactions
 */

document.addEventListener('DOMContentLoaded', () => {
    // 1. Navigation Header Scroll Effect
    const header = document.querySelector('.header');
    const scrollThreshold = 50;

    const checkScroll = () => {
        if (window.scrollY > scrollThreshold) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }
    };

    window.addEventListener('scroll', checkScroll);
    checkScroll(); // Run once in case page loads scrolled

    // 2. Mobile Menu Toggle
    const navToggle = document.querySelector('.nav-toggle');
    const navMenu = document.querySelector('.nav-menu');

    if (navToggle && navMenu) {
        navToggle.addEventListener('click', () => {
            navMenu.classList.toggle('active');
            
            // Toggle hamburger icon between ☰ and ✕
            const icon = navToggle.querySelector('i');
            if (icon) {
                if (navMenu.classList.contains('active')) {
                    icon.className = 'fas fa-times';
                } else {
                    icon.className = 'fas fa-bars';
                }
            }
        });

        // Close menu when clicking outside or on a link
        document.addEventListener('click', (e) => {
            if (!navToggle.contains(e.target) && !navMenu.contains(e.target)) {
                navMenu.classList.remove('active');
                const icon = navToggle.querySelector('i');
                if (icon) icon.className = 'fas fa-bars';
            }
        });
    }

    // 3. Scroll Reveal Animation (Intersection Observer)
    const animateElements = document.querySelectorAll('.reveal-on-scroll');
    
    if (animateElements.length > 0) {
        const revealCallback = (entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('revealed');
                    observer.unobserve(entry.target); // Animate only once
                }
            });
        };

        const revealObserver = new IntersectionObserver(revealCallback, {
            root: null, // viewport
            threshold: 0.15, // trigger when 15% is visible
            rootMargin: '0px 0px -50px 0px' // offset bottom trigger slightly
        });

        animateElements.forEach(el => revealObserver.observe(el));
    }

    // 4. Products Filter Tabs (Dynamic Client-side Filtering)
    const filterTabs = document.querySelectorAll('.product-tab');
    const productCards = document.querySelectorAll('.product-card');

    if (filterTabs.length > 0 && productCards.length > 0) {
        filterTabs.forEach(tab => {
            tab.addEventListener('click', () => {
                // Remove active class from all tabs
                filterTabs.forEach(t => t.classList.remove('active'));
                // Add active class to clicked tab
                tab.classList.add('active');

                const filterValue = tab.getAttribute('data-filter');

                productCards.forEach(card => {
                    const category = card.getAttribute('data-category');
                    
                    if (filterValue === 'all' || category === filterValue) {
                        card.style.display = 'block';
                        // Trigger tiny animation
                        card.style.opacity = '0';
                        setTimeout(() => {
                            card.style.opacity = '1';
                            card.style.transform = 'translateY(0)';
                        }, 50);
                    } else {
                        card.style.display = 'none';
                    }
                });
            });
        });
    }

    // 5. File Upload Feedback (Careers Page)
    const fileInput = document.getElementById('cv-file');
    const fileLabel = document.querySelector('.file-upload-label span');

    if (fileInput && fileLabel) {
        fileInput.addEventListener('change', (e) => {
            const fileName = e.target.files[0] ? e.target.files[0].name : 'Subir archivo CV (PDF/DOC)';
            fileLabel.textContent = fileName;
            fileLabel.style.color = 'var(--color-primary)';
            fileLabel.style.fontWeight = '600';
        });
    }
});
