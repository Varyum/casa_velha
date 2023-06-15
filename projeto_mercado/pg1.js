let slideIndex = 0;

showSlides();

function showSlides() {

    const slides = document.getElementsByClassName("mySlides");

    if (slideIndex < 0) {
        slideIndex = slides.length - 1;
    }

    if (slideIndex > slides.length - 1) {
        slideIndex = 0;
    }

    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    setInterval(function(){
        showSlides(slideIndex++)
    },4000)

    slides[slideIndex].style.display = "block";

}