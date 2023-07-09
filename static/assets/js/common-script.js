


$(window).load(function(){$(".loader").fadeOut("slow")});$(window).scroll(function(){var tsticky=$('#header'),scroll=$(window).scrollTop();if(scroll>=40){tsticky.addClass('header-fixed');$('#mrpt').show();$('#mmenu').hide()}else{tsticky.removeClass('header-fixed');$('#mrpt').hide();$('#mmenu').show()}});$(document).ready(function(){$('.dropdown').hover(function(){$(this).find('.dropdown-menu').first().stop(!0,!0).slideDown(150)},function(){$(this).find('.dropdown-menu').first().stop(!0,!0).slideUp(105)})});jQuery(document).ready(function($){var offset=300,offset_opacity=1200,scroll_top_duration=700,$back_to_top=$('.top-btn');$(window).scroll(function(){($(this).scrollTop()>offset)?$back_to_top.addClass('cd-is-visible'):$back_to_top.removeClass('cd-is-visible cd-fade-out');if($(this).scrollTop()>offset_opacity){$back_to_top.addClass('cd-fade-out')}});$back_to_top.on('click',function(event){event.preventDefault();$('body,html').animate({scrollTop:0,},scroll_top_duration)})});$(window).scroll(function(){var tsticky=$('.backto-top-btn'),scroll=$(window).scrollTop();if(scroll>=200)tsticky.addClass('backto-top-blk');else tsticky.removeClass('backto-top-blk')});$(document).ready(function(){$(".intonly").keypress(function(e){if(e.which!=8&&e.which!=0&&(e.which<48||e.which>57)){$("#errmsg").html("Digits Only").show().fadeOut("slow");return!1}})})

$(document).ready(function(){
	$(".srchBtn").click(function(){
		$("#fordesktop_searchBox").show(1000);
	})
	$("body").click(function(){
  		$(".autobox").fadeOut().removeClass("active");
	});
})