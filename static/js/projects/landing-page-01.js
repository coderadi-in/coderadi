const details = document.querySelectorAll('.main .faqs details');
details.forEach(detail => {
    detail.addEventListener('toggle', () => {
        if (detail.open) {
            detail.querySelector('.icon').style.transform = 'rotate(180deg)';
        } else {
            detail.querySelector('.icon').style.transform = 'rotate(0deg)';
        }
    });
});