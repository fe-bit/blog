var swiper = new Swiper(".slide", {
    slidesPerView: 3,
    spaceBetween: 20,
    loop: false,
    centerSlide: 'true',
    fade: 'true',
    grabCursor: 'false',
    pagination: {
        el: ".swiper-pagination",
        clickable: true,
        dynamicBullets: true,
    },
    navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
    },
    breakpoints: {
        0: {
            slidesPerView: 2,
        },
        520: {
            slidesPerView: 3,
        },
        950: {
            slidesPerView: 5,
        },
    },
});