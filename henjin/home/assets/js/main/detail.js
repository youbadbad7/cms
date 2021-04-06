

// 导航
var href_arr = location.href.split('/')
var last_href = location.href.split('/').pop()
var contain = href_arr.indexOf('article')
switch (last_href){
    case "product":
        $('.product a').addClass('bolder')
        break;
    case 'articles':
        $('.articles a').addClass('bolder')
        break;
    case 'about':
        $('.about a').addClass('bolder')
        break;
    case 'job':
        $('.job a').addClass('bolder')
        break;
    case '':
        $('.index a').addClass('bolder')
}
if(contain !=-1){
    $('.articles a').addClass('bolder')
}
