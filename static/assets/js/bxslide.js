



$(document).ready(function() {
    $('#bx1').bxSlider();
    $('#bx51').bxSlider();
    $('#bx2').bxSlider( {
        hideControlOnEnd: true, captions: true, pager: false
    }
    );
    $('#bx3').bxSlider( {
        hideControlOnEnd: true, minSlides: 3, maxSlides: 3, slideWidth: 360, slideMargin: 10, pager: false, nextSelector: '#bx-next', prevSelector: '#bx-prev', nextText: '>', prevText: '<'
    }
    );
    $('#bx4').bxSlider( {
        hideControlOnEnd: true, minSlides: 4, maxSlides: 4, slideWidth: 360, slideMargin: 10, pager: false, nextSelector: '#bx-next4', prevSelector: '#bx-prev4', nextText: '>', prevText: '<',
    }
    );
    // $('#bx5').bxSlider( {
    //     minSlides: 6, maxSlides: 6, slideWidth: 360, slideMargin: 5, pager: false, ticker: true, speed: 42000, tickerHover: true, useCSS: false
    // });

var maxSlides,
width = $(window).width();
if(window.matchMedia('(max-width: 767px)').matches) {
    maxSlides = 4;
} else {
    maxSlides = 6;
}
var myslider = $('#bx5').bxSlider({
    maxSlides: maxSlides,
     slideWidth: 160, slideMargin: 5, pager: false, ticker: true, speed: 82000, tickerHover: true, useCSS: false
});

var myslider1 = $('#bx51').bxSlider({
    maxSlides: maxSlides,
     slideWidth: 160, slideMargin: 5, pager: false, ticker: true, speed: 82000, tickerHover: true, useCSS: false
});

});
// if(window.matchMedia('(max-width: 767px)').matches) {
//     $('#bx5').bxSlider( {
//         minSlides: 2, maxSlides: 2, slideWidth: 360, slideMargin: 5, pager: false, ticker: true, speed: 42000, tickerHover: true, useCSS: false
//     }
//     );
// }


