// * NAVIGATION BAR TOGGLE SCRIPT
function toggle_sidebar() {
    const sidebar = document.querySelector('.nav');
    if (sidebar.classList.contains('open')) {
        sidebar.classList.remove('open');
        setTimeout(() => {
            sidebar.style.display = "none";
        }, 100);

    } else {
        sidebar.style.display = "flex";

        setTimeout(() => {
            sidebar.classList.add('open');
        }, 100);
    }
}

// & SIDEBAR BUTTON LISTENING SCIRPT
document.addEventListener('click', (e) => {
    if (e.target.closest('.menu-btn')) {
        toggle_sidebar();
    }
})