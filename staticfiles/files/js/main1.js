(function ($) {
    "use strict";
    /*--
        Menu Sticky
    -----------------------------------*/
    const $window = $(window);
    $window.on('scroll', function () {
        const scroll = $window.scrollTop();
        if (scroll < 300) {
            $(".sticker").removeClass("stick");
        } else {
            $(".sticker").addClass("stick");
        }
    });


    $('a[href*="#"]:not([href="#"])').click(function () {
        if (location.pathname.replace(/^\//, '') === this.pathname.replace(/^\//, '') && location.hostname === this.hostname) {
            let target = $(this.hash);
            target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
            if (target.length) {
                $('html, body').animate({
                    scrollTop: target.offset().top - 75
                }, 1000);
                return false;
            }
        }
    });
})(jQuery);



