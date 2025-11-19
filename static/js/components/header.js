// ? GETTING SIDEBAR ELEMENTS
const menuBtn = document.querySelector('.header .menu-btn');
const bar1 = document.querySelector('.header .bar1');
const bar2 = document.querySelector('.header .bar2');
const sidebar = document.querySelector('.sidebar');
const slideBtn = document.querySelector("#slide-nav");

// * NAVIGATION BAR TOGGLE SCRIPT
function toggle_sidebar() {    
    if (sidebar.classList.contains('open')) {
        sidebar.classList.remove('open');
        setTimeout(() => {
            sidebar.style.display = "none";
            menuBtn.style.gap = "10px";
            bar1.style.transform = "rotate(0)";
            bar2.style.transform = "rotate(0)";
        }, 100);

    } else {
        menuBtn.style.gap = "0";
        bar1.style.transform = "rotate(45deg)";
        bar2.style.transform = "rotate(-45deg)";
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

// & SLIDE BUTTON LISTENING SCRIPT
slideBtn.addEventListener('click', () => {
    toggle_sidebar();
})