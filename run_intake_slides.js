const intakeSlideContenair = document.querySelector(".intake-slide-container");
const intakeSlides = document.querySelectorAll(".intake-slide");
let intakeCurrentSlide = 0;
const intakSlideWidth = intakeSlides[0].clientWidth;

function showIntakeSlide(n){
    if (n < 0){
        intakeCurrentSlide = intakeSlides.length -1;

    }
    else if(n >= intakeSlides.length){
        intakeCurrentSlide = 0;
    }
    else{
        intakeCurrentSlide = n
    }

    const translateValue = -intakeCurrentSlide * intakSlideWidth + 'px';
    intakeSlideContenair.style.transform = 'translateX('+ translateValue + ')';

}

setInterval(() => {
    showIntakeSlide(intakeCurrentSlide + 1);
}, 5000);