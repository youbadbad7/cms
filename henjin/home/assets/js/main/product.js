var swiper = new Swiper('.swiper-container', {
    speed: 2000,
    pagination: {
        el: '.swiper-pagination',
        clickable: true
    },
    on: {
        slideChangeTransitionStart: function () {
            switch (this.activeIndex) {
                case 1:
                    if (!$('.des_Fiber').hasClass('clear_move')) {
                        $('.des_Fiber').addClass('clear_move')
                    }
                    break;
                case 2:
                    if (!$('.des_cotton').hasClass('clear_move')) {
                        $('.des_cotton').addClass('clear_move')
                    }
                    break;
                case 3:
                    if (!$('.desc_polyester .des_box').hasClass('clear_move')) {
                        $('.desc_polyester .des_box').addClass('clear_move')
                    }
                    break;
                case 4:
                    if (!$('.des_dye').hasClass('clear_move')) {
                        $('.des_dye').addClass('clear_move')
                    }
                    break;
                case 5:
                    if (!$('.desc_hamp .des_box').hasClass('clear_move')) {
                        $('.desc_hamp .des_box').addClass('clear_move')
                    }
                    break;
            }
        },
    },
    slidesPerView: 1,
    spaceBetween: 30,
    loop: true
});
