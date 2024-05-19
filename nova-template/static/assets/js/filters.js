$('.filter-button').on('click', function() {
    var filterValue = $(this).attr('data-filter');
    $('.item').hide(); 
    $(filterValue).show(); 
});