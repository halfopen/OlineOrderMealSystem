/**
 * Created by Administrator on 2015/12/17.
 * staff 相关业务的js
 */

is_submit = false;
var effects = new Array("fadeInRightBig", "fadeInLeftBig", "fadeInUpBig", "fadeInDownBig", "flip");

$(document).ready(function(){
    $(".staff-nav").addClass("active");
    $(".index-nav").removeClass("active");
    spin_color();
    $(".remove-meal").click(remove_booking);

    $(".table-list").click(select_table_list);
    $(".table-list-selected").click(unselect_table_list);

    $(".table_submit").on("click", booking_table);

    // 给meal-list添加动态载入特效
    $(".meal-list").each(function(index,value){
        console.log(index);
        console.log(value);
        $(this).removeClass("pulse");
        $(this).addClass(effects[ RandomNum(0,5) ]);

    });
    
});

function booking_table(){
    if(is_submit == false){
        is_submit = true;
    }else{
        return;
    }
    $("div.screen-mask").removeClass("none");
    r_id = $(".reservation").attr("r_id");
    tables_id ="0";
    $(".table-list-selected").each(function(index, value){
       tables_id+="-"+$(this).attr("pk");
    });
    $.ajax({
            type:"POST",
            url:"book_table/",
            //提交的数据
            data:{r_id:r_id, tables_id:tables_id},
            //返回数据的格式
            datatype: "json",//"xml", "html", "script", "json", "jsonp", "text".
            success:function(data){
            if(data == "True")
            {
                bootbox.alert("<h1>Ok</h1>", function() {
                    this.hide();
                    $(".screen-mask").addClass("none");
                    window.location.href="http://www.myooms.com:8000/staff/";
                });

            }
            else{
                bootbox.alert("<h1>"+data+"</h1>", function() {
                    this.hide();
                    $(".screen-mask").addClass("none");
                });
            }
            }   ,
            error: function(){
            }
    });
    is_submit = false;
}

function unselect_table_list(){
    total_size = $("#total_size").html();
    table_size = $(this).attr("size");
    total_size = parseInt(total_size);
    table_size = parseInt(table_size);
   // alert(total_size + " "+ table_size);
    t = 0;
    t = total_size - table_size;
    $(this).addClass("table-list");
    $(this).removeClass("table-list-selected");
    $(this).unbind("click", unselect_table_list);
    $(this).bind("click",select_table_list);
    $("#total_size").html(t);

    number = parseInt($(".reservation_number").attr("number"));

    if(t >= number){
        $(".book_table").addClass("btn-green");
        $(".book_table").addClass("table_submit");
        $(".book_table").bind("click", booking_table);
    }else{
        $(".book_table").removeClass("btn-green");
        $(".book_table").removeClass("table_submit");
        $(".book_table").unbind("click", booking_table);
    }
}

function select_table_list(){
    total_size = $("#total_size").html();
    table_size = $(this).attr("size");
    total_size = parseInt(total_size);
    table_size = parseInt(table_size);
    //alert(total_size + " "+ table_size);
    t = 0;
    t = total_size + table_size;
    $(this).addClass("table-list-selected");
    $(this).removeClass("table-list");

    $(this).unbind("click",select_table_list);
    $(this).bind("click", unselect_table_list);
    $("#total_size").html(t);

    number = parseInt($(".reservation_number").attr("number"));

    if(t >= number){
        $(".book_table").addClass("btn-green");
        $(".book_table").addClass("table_submit");
        $(".book_table").bind("click", booking_table);
    }else{
        $(".book_table").removeClass("btn-green");
        $(".book_table").removeClass("table_submit");
        $(".book_table").unbind("click", booking_table);
    }
}

function spin_color(){
    console.log("spin");
    $(".spin img").each(function(i){
        i = parseInt(Math.random()*6)+1;
        path = "http://www.myooms.com:8000/static/img/spin/"+i+".png";
        $(this).attr("src", path);
        $(this).addClass("animated");
        $(this).addClass("fadeInDownBig");

        console.log($(this));
  });
}

// 移除订单
function remove_booking(){
    //alert("remove");
    r_id = $(this).attr("pk");
    t = $(this).parent(".meal-list");
    t.removeClass("pulse");
    t.addClass("slideOutUp").fadeOut(800);
    //return;
    $.ajax({
            type:"POST",
            url:"cancel/",
            //提交的数据
            data:{id:r_id},
            //返回数据的格式
            datatype: "json",//"xml", "html", "script", "json", "jsonp", "text".
            success:function(data){
            if(data == "True")
            {
                bootbox.alert("<h1>移除成功</h1>", function() {
                    console.log("ok");
                });
            }
            else{
                alert("移除失败");
            }
            }   ,
            error: function(){
            }
    });

}

