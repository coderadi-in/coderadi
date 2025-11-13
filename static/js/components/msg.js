const alerts = document.querySelectorAll(".alert");

// * NOTIFICATION DISPLAY ANIMATION SCRIPT
function animate(index=0) {
    if (index >= alerts.length) {return;}

    alerts[index].style.transform = "translateX(0)";

    setTimeout(() => {
        animate(index+1);
    }, 100);
}

// * NOTFICATION SLIDEOUT ANIMATION SCRIPT
function deanimate(index=0) {
    if (index >= alerts.length) {return;}

    alerts[index].style.transform = "translateX(-110%)";

    setTimeout(() => {
        deanimate(index+1);
    }, 100);
}

setTimeout(() => {
    animate();
}, 100);

setTimeout(() => {
    deanimate();
}, 3000);