// ? GETTING SKILLS ELEMENTS
const skillBars = document.querySelectorAll('.skill-display');
const frontendCont = document.querySelector('.desc#frontend');
const backendCont = document.querySelector('.desc#backend');
const DSCont = document.querySelector('.desc#data-science');
const hoverContent = document.querySelector('#hover');

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
                            showCursor: false,

                            // onComplete: function() {
                            //     setTimeout(() => {
                            //         render_skill_chart();
                            //     }, 1000);
                            // }
                        })
                    }, 1000);
                }
            })
        }, 1000);
    }
});

// * SKILLBARS DISPLAY ANIMATION SCRIPT
function displaySkillBars(index=0) {
    if (index >= skillBars.length) {return;}

    skillBars[index].classList.add('show');

    setTimeout(() => {
        displaySkillBars(index+1);
    }, 100);
}

// & ELEMENT OBSERVER SCRIPT
const observer = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            if (entry.target.classList.contains('skills')) {
                displaySkillBars();
            }
        }
    });
}, {
    root: null,
    threshold: 0.2
});

// & SCRIPT TO USE THE OBSERVER TO OBSERVE .SECTION
sections = document.querySelectorAll(".main section");
sections.forEach((section) => {
    observer.observe(section);
})

// * FUNCTION TO HIDE SKILL DESCRIPTIONS
function hideSkillDesc() {
    hoverContent.style.display = "none";
    frontendCont.style.display = "none";
    backendCont.style.display = "none";
    DSCont.style.display = "none";

    hoverContent.style.opacity = "0";
    frontendCont.style.opacity = "0";
    backendCont.style.opacity = "0";
    DSCont.style.opacity = "0";
}

// & EVENT LISTENERS FOR SKILLBAR CLICKS
skillBars.forEach((bar) => {
    bar.addEventListener('click', () => {
        hideSkillDesc();
        if (bar.classList.contains('frontend')) {
            frontendCont.style.display = "flex";

            setTimeout(() => {
                frontendCont.style.opacity = "1";
            }, 100);
        }

        if (bar.classList.contains('backend')) {
            backendCont.style.display = "flex";

            setTimeout(() => {
                backendCont.style.opacity = "1";
            }, 100);
        }

        if (bar.classList.contains('data-science')) {
            DSCont.style.display = "flex";

            setTimeout(() => {
                DSCont.style.opacity = "1";
            }, 100);
        }
    })
});