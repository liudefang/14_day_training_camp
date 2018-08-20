$(function () {

    //模态窗中的标签样式切换
    $('.pull-left .my-modal-body ul li').click(function () {
        $(this).addClass('active').sibling('li').removeClass('active');
        $($('.my-modal-body ul').sibling('div')[$(this).index()]).show().sibling('div').hide();

    });

})

//注册登录页面
function login() {
    $('#myModal').modal({
        keyboard:false
    });
    /*为了弹出框，弹出时滚动条不消失，背景不影响*/
    $('body').css('padding-right','0')

}