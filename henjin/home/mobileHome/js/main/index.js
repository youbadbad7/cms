
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

var swiper = new Swiper('.swiper-banner',{
    speed: 1000,
    slidesPerView: 1,
    loop: true
});

var swiper1 = new Swiper('.swiper-info', {
    slidesPerView: 3,
    spaceBetween: 30,
    freeMode : true,
    slidesOffsetBefore:0

});

var swiper2 = new Swiper('.swiper-info1', {
    slidesPerView: 3,
    spaceBetween: 30,
    freeMode : true,
    slidesOffsetBefore:0
});

window.onload = function () {
    var ie=navigator.appName=="Microsoft Internet Explorer" ? true : false;
    var a=document.createEvent("MouseEvents");//FF的处理
    a.initEvent("click", true, true);
    document.getElementsByClassName('welcome_video')[0].dispatchEvent(a);
}

if(!localStorage.hasPlay){
    localStorage.hasPlay = '1'
    $('.index_video').css('display','block')
}
if($('.index_video').css('display')!='none'){
    $('.nav_main').css('display','none')
}
$('.video_close').click(function () {
    $('.nav_main').css('display','none')
    $('.index_video').css('display','none')
})

$('.video_icon img').click(function () {
    $('.index_video').css('display','block')
    $('.nav_main').css('display','none')
})