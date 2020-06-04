$(document).ready(function(){
    $(document).on('submit', 'form', function(event){
        $()
            $.ajax({
                data: {
                    name: $('#name').val(),
                    designation: $('#designation').val(),
                    address: $('#address').val(),
                    phone: $('phone').val()
                },
                type: 'POST',
                url : '/'
            })
        .done(function(data))
        event.preventDefault();
    })
})