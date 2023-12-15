

const slidesContainer = document.querySelector('.slides-container');
const slides = document.querySelectorAll('.slide');
let currentSlide = 0;
const slideWidth = slides[0].clientWidth;

function showSlide(n) {
  if (n < 0) {
    currentSlide = slides.length - 1;
  } else if (n >= slides.length) {
    currentSlide = 0;
  } else {
    currentSlide = n;
  }

  const translateValue = -currentSlide * slideWidth + 'px';
  slidesContainer.style.transform = 'translateX(' + translateValue + ')';
}

setInterval(() => {
  showSlide(currentSlide + 1);
}, 5000);