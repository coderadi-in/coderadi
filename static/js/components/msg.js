const alerts = document.querySelectorAll(".alert");

// * NOTIFICATION DISPLAY ANIMATION SCRIPT
function animate(index=0) {
    if (index >= alerts.length) {return;}

    alerts[index].classList.add("show");

    setTimeout(() => {
        animate(index+1);
    }, 100);
}

// * NOTFICATION SLIDEOUT ANIMATION SCRIPT
function deanimate(index=0) {
    if (index >= alerts.length) {return;}

    alerts[index].classList.remove("show");

    setTimeout(() => {
        alerts[index].style.display = "none";
        deanimate(index+1);
    }, 100);
}

setTimeout(() => {
    animate();
}, 100);

setTimeout(() => {
    deanimate();
}, 3000);