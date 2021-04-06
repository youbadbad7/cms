var swiper1 = new Swiper('.swiper-container', {
    autoplay: true,
    speed: 1000,
    slidesPerView: 1,
    loop: true,
    pagination: {
        el: '.swiper-pagination',
    }
});

var job_des = []
var names = []
var job_special = {}
var job_html = ''
var all_name = {}
$.get('/api/job', function (data) {

    all_name = data
    names = data.station_names
    console.log(names);
    return;
    $.each(data, function (k, v) {
        if (v.constructor != Array) {
            job_des.push(v)
        }
    })
    $.each(names, function (k, v) {
        var name_html;
        if (k == 0) {
            name_html = '<div class="job_name active">' + v.name + '</div>'
        } else {
            name_html = '<div class="job_name">' + v.name + '</div>'
        }

        $('.job_list').append(name_html)
    })
    job_special = data[0]
    job_html = '<div class="special">' +
        '<div class="name">需求专业:</div>' +
        '<div class="part">' + job_special.special + '</div>' +
        '</div>' +
        '<div class="treatment">' +
        '<div class="name">福利待遇:</div>' +
        '<div class="part">' + job_special.treatment + '</div> ' +
        '</div> ' +
        '<div class="requirement"> ' +
        '<div class="name">工作要求:</div> ' +
        '<div class="part">' + job_special.requirement + '</div> ' +
        '</div>'
    $('.job_desc').append(job_html)
})

$(document).on('click', '.job_name', function () {
    var index = $(this).index()
    $(this).addClass('active').siblings().removeClass('active')
    job_special = all_name[index]
    $('.job_desc').html('')
    job_html = '<div class="special">' +
        '<div class="name">需求专业:</div>' +
        '<div class="part">' + job_special.special + '</div>' +
        '</div>' +
        '<div class="treatment">' +
        '<div class="name">福利待遇:</div>' +
        '<div class="part">' + job_special.treatment + '</div> ' +
        '</div> ' +
        '<div class="requirement"> ' +
        '<div class="name">工作要求:</div> ' +
        '<div class="part">' + job_special.requirement + '</div> ' +
        '</div>'
    $('.job_desc').append(job_html)
})