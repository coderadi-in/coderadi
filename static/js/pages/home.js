// & TYPING ANIMATION SCRIPT FOR HERO SECTION
var typed = new Typed('#type-1', {
    strings: ['Hi,'],
    typeSpeed: 30,

    onComplete: function() {
        setTimeout(() => {

            document.querySelector('#type-1').nextSibling.style.display = 'none';
            var typed2 = new Typed("#type-2", {
                strings: ["I'm <span id='highlight' data-text='Aditya'>Aditya</span>."],
                typeSpeed: 30,

                onComplete: function() {
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

// * CHART INTEGRATION SCRIPT
function render_skill_chart() {
    const ctx = document.querySelector("#skill-chart").getContext('2d');
    const chart = new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: ['HTML', 'CSS', 'JS', 'Flask', 'Flet'],
            datasets: [{
                label: 'My skillset',
                data: [20, 25, 10, 35, 10],
                backgroundColor: [
                    "#32A852",
                    "#3250A8",
                    "#D14949",
                    "#DEA16D",
                    "#1A1A1D",
                ],
                borderColor: "transparent",
                hoverOffset: 5
            }]
        }
    })
}

// * PROJECT DISPLAY ANIMATION SCRIPT
const projects = document.querySelectorAll('.project');
function display_projects(index=0) {
    if (index >= projects.length) {return;}

    projects[index].classList.add('visible');

    setTimeout(() => {
        display_projects(index+1);
    }, 200);
}

// & ELEMENT OBSERVER SCRIPT
const observer = new IntersectionObserver((entries, observer) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {      
      if (entry.target.classList.contains('projects')) {
        display_projects();
      }
    }
  });
}, {
  root: null,
  threshold: 0.2
});

// & SCRIPT TO USE THE OBSERVER TO OBSERVE .SECTION
// sections = document.querySelectorAll(".section");
// sections.forEach((section) => {
//     observer.observe(section);
// })