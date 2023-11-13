     // jQuery code to add 'active' class on menu item click
     $(document).ready(function() {
        $('.nav-item').click(function() {
            $('.nav-item').removeClass('active');
            $(this).addClass('active');
        });
    });