/*
 *  jodstrap
 *  Copyrights - saltflakes.net
 *  Creator: saltflakes.net
 *  January 2013
 */ 
 

$(document).ready(function() {

	// bxslider options:
	$('.bxslider').bxSlider({
		minSlides : 3,
		maxSlides : 4,
		slideWidth : 170,
		slideMargin : 10,
		pager : false
	});

	// lavalamp navigation and options:
	if ($().lavaLamp) {
		$('.navanimation').lavaLamp({
			fx : 'swing',
			speed : 400
		});
	}

	// camera slider options:
	if ($('#camera_wrap_1').length > 0) {
		$('#camera_wrap_1').camera({
			thumbnails : true,
			height : '35%',
			loader : 'none',
			opacityOnGrid : false,
			onLoaded : function() {				
			}
		});
	}
	// camera slider for single portfolio options:
	if ($('#camera_wrap_2').length > 0) {
		$('#camera_wrap_2').camera({
			thumbnails : false,
			pagination : false,
			fx : 'scrollHorz',
			transPeriod : 800,
			height : '70%',
			loader : 'none',
			opacityOnGrid : false,
			onLoaded : function() {

			}
		});
	}
	
	//Submenu effect:
	$(".open-submenu").hover(function() {
		$(this).children("ul").stop(true, true).slideDown();
	}, function() {
		$(this).children("ul").stop(true, true).slideUp();
	});
	
	//Twitter scroll effect:
	function tick() {
		$('ul#twitter-ticker li:first').slideUp('slow', function() {
			$(this).appendTo($('ul#twitter-ticker')).fadeIn('slow');
		});
	}
	setInterval(function() {
		tick()
	}, 5000);

	//isotope filter portfolio2:
	$(".sf-da-isotope").isotope({
		//options
		itemSelector : '.sf-da-item',
		layoutMode : 'fitRows',
	});

	// filter items when filter link is clicked:
	$('#da-filters a').click(function() {
		var selector = $(this).attr('data-filter');
		$(".sf-da-isotope").isotope({
			filter : selector
		});
		$('.sf-da-isotope-filters li').removeClass("active");
		$(this).closest('li').addClass("active");
		return false;
	});
	$(' #da-thumbs > li ').each(function() {
		$(this).hoverdir();
	});

	//isotope filter options:
	$(".sf-isotope").isotope({
		itemSelector : '.sf-item',
		layoutMode : 'fitRows',
	});
	$(window).resize();
	var $container = $('.sf-isotope')
	$container.isotope({
		// options...
		resizable : false, // disable normal resizing
		masonry : {
			columnWidth : $container.width() / 5
		}
	});
	// isotope - update columnWidth on window resize
	$(window).smartresize(function() {
		$container.isotope({
			// update columnWidth to a percentage of container width
			masonry : {
				columnWidth : $container.width() / 5
			}
		});
	});

	// isotope - filter items when filter link is clicked:
	$('#filters a').click(function() {
		var selector = $(this).attr('data-filter');
		$(".sf-isotope").isotope({
			filter : selector
		});
		$('.sf-isotope-filters li').removeClass("active");
		$(this).closest('li').addClass("active");
		return false;
	});

	// portfolio sf item hover:
	$(".sf-item").hover(function() {
		$(this).children().children('.sf-item-overlay').stop(true, true).animate({
			'opacity' : '1'
		}, 400);
		$(this).children().children('.sf-item-text').stop(true, true).animate({
			'color' : '#FFFFFF'
		}, 400);
	}, function() {
		$(this).children().children('.sf-item-overlay').stop(true, true).animate({
			'opacity' : '0'
		}, 400);
		$(this).children().children('.sf-item-text').stop(true, true).animate({
			'color' : '#222222'
		}, 400);
	});
	
	// jquery form validator:
	$('#sf-form').validate({
		submitHandler : function(form) {
			form.submit();
		}
	});
	
	// bootstrap extension datepicker:
	$('.datepicker').datepicker();
	
	// bootstrap tabs:
	$('#sf-tab a').click(function(e) {
		e.preventDefault();
		$(this).tab('show');
	})
	$('#sf-tab a:first').tab('show');
	
	// bootstrap tooltips:
	$('.sf-tooltip').tooltip();
	
	// bottstrap popover:
	$('.sf-popover').popover();
	
	// colorbox:
	$('.sf-colorbox').colorbox();
	
});

// responsive mobile navigation:
selectnav('sf-menu-responsive'); 