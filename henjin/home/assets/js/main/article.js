$(function () {
    $(".search-img").hover(function () {
        $(this).find("input").focus().addClass("active");
    }, function () {
        $(this).find("input").blur().removeClass("active");
    });

    $("#search").click(function () {
        var keyword = $('input[name="keyword"]').val();
        if (keyword == "") {
            alert("请输入要搜索的标题");
            return false;
        }
        var action = "/search?keyword=" + keyword;
        $("#form").attr('action', action).submit();
    })


})

