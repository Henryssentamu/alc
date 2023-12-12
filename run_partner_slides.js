// let currentSlide = 0;
// const slideInterval = 5000; // Change this value to set the time interval in milliseconds

// function changeSlide(n) {
//     showSlide(currentSlide += n);
// }

// function showSlide(n) {
//     const slides = document.querySelectorAll('.slide');
//     if (n >= slides.length) {
//     currentSlide = 0;
//     }
//     if (n < 0) {
//     currentSlide = slides.length - 1;
//     }

//     slides.forEach(slide => {
//     slide.classList.remove('active');
//     });

//     slides[currentSlide].classList.add('active');
// }

// // Automatically change the slide at the specified interval
// setInterval(() => {
//   changeSlide(1); // Change by 1 to go to the next slide
// }, slideInterval);

// let currentGroup = 0;
// const slides = document.querySelectorAll('.slide');
// const slidesPerGroup = 3;
// const slideInterval = 5000; // Change this value to set the time interval in milliseconds

// function changeGroup() {
//   const start = currentGroup * slidesPerGroup;
//   const end = start + slidesPerGroup;

//   for (let i = 0; i < slides.length; i++) {
//     if (i >= start && i < end) {
//       slides[i].classList.add('active');
//     } else {
//       slides[i].classList.remove('active');
//     }
//   }

//   currentGroup = (currentGroup + 1) % Math.ceil(slides.length / slidesPerGroup);
// }

// // Automatically change the slide group at the specified interval
// setInterval(() => {
//   changeGroup();
// }, slideInterval);

// let currentGroup = 0;
// const slidesContainer = document.querySelector('.presentation');
// const slides = document.querySelectorAll('.slide');
// const slidesPerGroup = 3;
// const slideInterval = 5000; // Change this value to set the time interval in milliseconds

// function changeGroup() {
//   const start = (currentGroup * slidesPerGroup) % slides.length;
//   const end = (start + slidesPerGroup) % slides.length;

//   for (let i = 0; i < slides.length; i++) {
//     if (i >= start && i < end) {
//       slides[i].classList.add('active');
//     } else {
//       slides[i].classList.remove('active');
//     }
//   }

//   // Move the first slide to the end of the container
//   slidesContainer.appendChild(slides[start].cloneNode(true));
//   slidesContainer.removeChild(slides[start]);

//   currentGroup = (currentGroup + 1) % slides.length;
// }

// // Automatically change the slide group at the specified interval
// setInterval(() => {
//   changeGroup();
// }, slideInterval);

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