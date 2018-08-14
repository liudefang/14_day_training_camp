window.onload = function () {

    var path = window.location.href.substring(0,window.location.href.lastIndexOf('/'));

    //右上方购物车换图片
    var cartA = document.getElementsByClassName('topbar-cart')[0].children[0];
    cartA.onmouseover = function () {
        cartA.children[0].style.background = 'url("'+path+'/imgs/icon-shop2.png") 3px 24px';
    };
    cartA.onmouseout = function () {
        cartA.children[0].style.background = 'url("'+path+'/imgs/icon-shop1.png") 3px 24px';
    };

    //搜索框样式js
    var searchStyle = document.getElementById('search');
    var submitStyle = document.getElementById('submit');
    var hotWords = document.getElementsByClassName('hot-words')[0];
    searchStyle.onmouseover = function () {
        searchStyle.style.border = '1px solid #b0b0b0';
        submitStyle.style.border = '1px solid #b0b0b0';
    };
    searchStyle.onmouseout = function () {
        searchStyle.style.border = '1px solid #e0e0e0';
        submitStyle.style.border = '1px solid #e0e0e0';
    };
    searchStyle.onclick = function () {
        searchStyle.style.border = '1px solid rgba(255,103,0,0.98)';
        submitStyle.style.border = '1px solid rgba(255,103,0,0.98)';
        hotWords.style.display = 'none';
    };

    //轮播图
    var count = 0;
    var imgStyle = document.getElementsByClassName('up-r')[0].children[0].children;

    setInterval(function () {
        for(var m=0;m<imgStyle.length;m++){
            imgStyle[m].style.display = 'none';
        }
        imgStyle[count].style.display = 'block';
        count++;
        count === 3 ? count = 0 : count;
    },2000);

    //上方ul li 移上去换图片
    var headerli = document.getElementsByClassName('header-nav')[0].children[0].children;
    for(var k=0;k<headerli.length;k++){
        headerli[k].onmouseover = function () {
             this.children[1].style.display = 'block';
        };
        headerli[k].onmouseout = function () {
             this.children[1].style.display = 'none';
        };
    }

    //左侧列表ul li 移上去显示框
    var liAddActive = document.getElementsByClassName('up-l')[0].children[0].children;
    for(var i=0;i<liAddActive.length;i++){
        liAddActive[i].onmouseover = function () {
            this.children[2].className = 'active';
        };
        liAddActive[i].onmouseout = function () {
            this.children[2].className = '';
        }
    }

    //左侧下方ul li 移上去换图片
    var downLeftli = document.getElementsByClassName('down-l')[0].children[0].children;
    for(var j=0;j<downLeftli.length;j++){
        downLeftli[j].onmouseover = function () {
            this.children[0].children[0].style.background = 'url("'+path+'/imgs/icon-small2.png") no-repeat center';
        };
        downLeftli[j].onmouseout = function () {
            this.children[0].children[0].style.background = 'url("'+path+'/imgs/icon-small1.png") no-repeat center';
        };
    }

    //右侧固定栏目得js
    var right_ul = document.getElementById('right-ul');
    var oBarRight_img = document.getElementsByClassName('fixed-1-img')[0];
    var fixed_1 = document.getElementsByClassName('fixed-1')[0];
    var fixed_2 = document.getElementsByClassName('fixed-2')[0];
    right_ul.children[0].onmouseover = function () {
        oBarRight_img.style.display = 'block';
        fixed_1.style.background = 'url("'+path+'/imgs/fixed-1c.png") no-repeat center center/30px';
    };
    right_ul.children[0].onmouseout = function () {
        oBarRight_img.style.display = 'none';
        fixed_1.style.background = 'url("'+path+'/imgs/fixed-1.png") no-repeat center center/30px';
    };
    right_ul.children[1].onmouseover = function () {
        fixed_2.style.background = 'url("'+path+'/imgs/fixed-2c.png") no-repeat center center/30px';
    };
    right_ul.children[1].onmouseout = function () {
        fixed_2.style.background = 'url("'+path+'/imgs/fixed-2.png") no-repeat center center/30px';
    };

};