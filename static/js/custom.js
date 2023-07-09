$('html, body').css({
    'overflow': 'hidden',
    'height': '100%'
})
$('html, body').removeAttr('style')

function onlyNos(e, t) {
    try {
        if (window.event) {
            var charCode = window.event.keyCode
        } else if (e) {
            var charCode = e.which
        } else {
            return !0
        }
        if (charCode > 31 && (charCode < 48 || charCode > 57)) {
            return !1
        }
        return !0
    } catch (err) {
        alert(err.Description)
    }
}
$("#pay1").click(function() {
    $(this).prop('checked', !0);
    $('#pay2').prop('checked', !1)
});
$("#pay2").click(function() {
    $(this).prop('checked', !0);
    $('#pay1').prop('checked', !1)
});

function lookup(inputString) {	
    if (inputString.length == 0) {
        $('#typrch').hide()
    } else { 
        quickAjaxLookUp = $.ajax({
            url: "custresech.php",
            type: "POST",
            data: {
                key: "" + inputString + ""
            },
            beforeSend: function() {
                if (typeof quickAjaxLookUp !== "undefined") {
                    quickAjaxLookUp.abort()
                }
            },
            success: function(data) {
                $('.typrch').show();
                $('.typrch').html(data)
            }
        })
    }
}
$("#catpage").val() > 0 && ($("#aboutt").readmore({
    speed: 75,
    collapsedHeight: 85
}))
$("#catlst").click(function() {
    $(this).hide();
    $(".catbot").show()
});
$("#clkbot").click(function() {
    $(this).hide();
    $(".catbot").hide();
    $("#catmain").show();
    $("#catlst").show()
});

jQuery("#t-carousel").owlCarousel({
  autoplay: true,
  lazyLoad: true,
  loop: true,
  margin: 20,
   /*
  animateOut: 'fadeOut',
  animateIn: 'fadeIn',
  */
  responsiveClass: true,
  autoHeight: true,
  autoplayTimeout: 7000,
  smartSpeed: 800,
  responsive: {
    0: {
      items: 1
    },

    600: {
      items: 2
    },

    1024: {
      items: 3
    },

    1366: {
      items: 3
    }
  }
});



$(document).ready(function(){
	$(".srchBtn").click(function(){
		$("#fordesktop_searchBox").show(1000);
		$(".srchBtn").hide();
		$(".srchcloseBtn").show();
	})
	$(".srchcloseBtn").click(function(){
		$("#fordesktop_searchBox").hide(1000);
		$(".srchBtn").show();
		$(".srchcloseBtn").hide();
	})
	$("body").click(function(){
  		$(".autobox").fadeOut().removeClass("active");
	});
})

$(document).ready(function() {

  $(".toggle-accordion").on("click", function() {
    var accordionId = $(this).attr("accordion-id"),
      numPanelOpen = $(accordionId + ' .collapse.in').length;
    
    $(this).toggleClass("active");

    if (numPanelOpen == 0) {
      openAllPanels(accordionId);
    } else {
      closeAllPanels(accordionId);
    }
  })

  openAllPanels = function(aId) {
    console.log("setAllPanelOpen");
    $(aId + ' .panel-collapse:not(".in")').collapse('show');
  }
  closeAllPanels = function(aId) {
    console.log("setAllPanelclose");
    $(aId + ' .panel-collapse.in').collapse('hide');
  }
     
});