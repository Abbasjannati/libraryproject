document.querySelectorAll('.book-card').forEach(card => {
    card.addEventListener('mouseenter', function() {
        this.style.transform = 'scale(1.02)';
        this.style.transition = 'transform 0.2s';
    });
    card.addEventlisterner('mouseleave', function() {
        this.style.transform = 'scale(1)';
    });
});