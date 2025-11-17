// & TYPING ANIMATION SCRIPT FOR HERO SECTION
var typed = new Typed('#type-1', {
    strings: ['Hi,'],
    typeSpeed: 30,

    onComplete: function () {
        setTimeout(() => {

            document.querySelector('#type-1').nextSibling.style.display = 'none';
            var typed2 = new Typed("#type-2", {
                strings: ["I'm <span id='highlight' data-text='Aditya'>Aditya</span>."],
                typeSpeed: 30,

                onComplete: function () {
                    setTimeout(() => {

                        document.querySelector('#type-2').nextSibling.style.display = 'none';
                        var typed3 = new Typed("#type-3", {
                            strings: ["A dedicated software developer &amp; entrepreneur."],
                            typeSpeed: 30,
                            showCursor: false
                        })
                    }, 1000);
                }
            })
        }, 1000);
    }
});

// // & ELEMENT OBSERVER SCRIPT
// const observer = new IntersectionObserver((entries, observer) => {
//     entries.forEach(entry => {
//         if (entry.isIntersecting) {
//             if (entry.target.classList.contains('skills')) {
//                 displaySkillBars();
//             }
//         }
//     });
// }, {
//     root: null,
//     threshold: 0.2
// });

// // & SCRIPT TO USE THE OBSERVER TO OBSERVE .SECTION
// sections = document.querySelectorAll(".main section");
// sections.forEach((section) => {
//     observer.observe(section);
// })