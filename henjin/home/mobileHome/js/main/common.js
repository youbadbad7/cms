$('.nav-icon').click(function () {
    $(this).toggleClass('close')
    if($(this).html()==''){
        $(this).html('MENU')
    }else {
        $(this).html('')
    }
    $(this).next().slideToggle()
})