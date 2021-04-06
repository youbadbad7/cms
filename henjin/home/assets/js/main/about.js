$(".search-img").hover(function () {
    $(this).find("input").focus().addClass("active");
}, function () {
    $(this).find("input").blur().removeClass("active");
});
