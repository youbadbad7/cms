var position = [200, 400, 900, 1800];
var initTop = $(window).scrollTop()
for (var i = 0; i < position.length; i++) {
    if (initTop > position[i]) {
        $(".move_box").eq(i).addClass('animated fadeInUp op_one');
    }
}
var swiper1 = new Swiper('.swiper-container', {
    speed: 1000,
    slidesPerView: 1,
    loop: true,
    navigation: {
        nextEl: '.swiper-prev',
        prevEl: '.swiper-next',
    }
});

var swiper2 = new Swiper('.swiper-info', {
    speed: 1500,
    slidesPerView: 1,
    loop: true,
    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
    },
});

// const element =  document.querySelector('#main_about .content')
// element.classList.add('animated', 'fadeInUp')

var index = 0;
$(window).scroll(function () {
    var top = $(window).scrollTop();
    if (top > position[index]) {
        $(".move_box").eq(index).addClass('animated fadeInUp op_one');
        index++;
    }
})

$('.chang_lan').click(function () {
    // $('.chang_lan>a').toggleClass('highlight')
})

$('.chang_cn').click(function () {
    $('.info.cn').addClass('active')
    $('.info.en').removeClass('active')
    $(this).addClass('highlight').siblings().removeClass('highlight')
})
$('.chang_en').click(function () {
    $('.info.en').addClass('active')
    $('.info.cn').removeClass('active')
    $(this).addClass('highlight').siblings().removeClass('highlight')
})

//欢迎视频相关

//视频显示
if(!localStorage.hasPlay){
    localStorage.hasPlay = '1'
    $('.index_video').css('display','block')
}
//播放完成后
if($('.index_video').css('display')!='none'){
    $('.nav_main').css('display','none')
}
$('.video_close').click(function () {
    $('.index_video').css('display','none')
    $('.nav_main').css('display','block')
})

$('.video_icon img').click(function () {
    $('.index_video').css('display','block')
    $('.nav_main').css('display','none')
})

