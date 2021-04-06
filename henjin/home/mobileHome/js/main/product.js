
// 导航
var last_href = location.href.split('/').pop()
switch (last_href){
    case "product":
        $('#mb_nav .product a').addClass('active')
        break;
    case 'articles':
        $('#mb_nav .articles a').addClass('bolder')
        break;
    case 'about':
        $('#mb_nav .about a').addClass('bolder')
        break;
    case 'job':
        $('#mb_nav .job a').addClass('bolder')
        break;
    case '':
        $('#mb_nav .index a').addClass('bolder')
}