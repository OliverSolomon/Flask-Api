$(".toggle-icon").on('click', function() {
            $('#nav-container ').toggleClass("pushed");



            $('.sidebar ,.left-items').slideToggle(500);
            $('.sidebar').css('filter', 'blur(0)');
            $('.linux-menu,.windows-menu,.hacks-menu').hide();
            $('.sidebar a').on('mouseover click', function() {
                var current = $(this).attr('id'); //GETS CURRENT HOVERED OVER LINK ID
                $("." + current + '-menu').show(400);
            });
            $("." + current + '-menu').mouseleave(function() {
                $("." + current + '-menu').hide(400);

            });
        });
