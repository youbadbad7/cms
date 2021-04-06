

// 导航
var last_href = location.href.split('/').pop()
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