
var nStart = 6;
$('#loadMore').click(function () {
    var _this = $('.news_lists');
    if (nStart >= "{!! $total !!}") {
        $(".more").text('没有数据');
        return false;
    } else {
        $.post("/getMore", {page: nStart}, function (data) {
            // console.log(data);return;
            $.each(data, function (i, item) {
                _this.append('<div class="list_item">' +
                    '<div class="title">'+
                        '<h2>' + item.time + '</h2>' +
                        '<div><a href="/article/' + item.id + '">' + item.title + '</a></div>' +
                    '</div>'+
                    '<p>' + item.body + '</p>' +
                    '</div>');
            });
        });
        nStart += 6;
    }
})

$(function () {
    $("#search").click(function () {
        var keyword = $('input[name="keyword"]').val();
        var action = "/search?keyword=" + keyword;
        $("#form").attr('action', action).submit();
    })
})


//解决419
$.ajaxSetup({headers: {'X-CSRF-TOKEN': $('meta[name="csrf-token"]').attr('content')}})