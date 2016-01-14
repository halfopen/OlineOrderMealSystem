$(document).ready(function(){
    $(".export_excel").on("click", export_excel);
    $(".submit-suggestion").on("click", submit_suggestion);
    $(".free-tables-search").on("click", get_free_tables);



});


function get_free_tables(){
    time = $(".search-time").val();
    date = $(".search-date").val();
    $("div.screen-mask").removeClass("none");
    datas = {time:time, date:date};
    table_container = $(".free-tables-container");
    reservations_container = $(".reservations-container");
    var effects = new Array("bounceIn","bounceInDown","bounceInLeft","bounceInRight","bounceInUp"); // 出现特效
    $.ajax({
        type:"POST",
        url:"./",
        data:datas,
        datatype: "html",//"xml", "html", "script", "json", "jsonp", "text".
        success:function(data){
            if(data=="False"){
                bootbox.alert("<h1>请输入搜索条件</h1>", function() {
                    this.hide();
                });
            }else{
                //console.log(data);

                data = data.replace("\"","" );
                tables = data.split(",");
                table_container.html(" ");
                for(i=0;i<tables.length-1;i++){
                    table_num = parseInt(tables[i]);
                    console.log(table_num);
                    table_html = $('<div class="animated col-md-1 text-center meal-list table-list">' +
                            '<a style="color:white" target="_blank" href="../staff/table_detail?id='+table_num+'">'+table_num+'号桌子</a></div>');
                    //table_html.hide();
                    table_container.append( table_html);

                    table_html.addClass(effects[RandomNum(0,5)]);
                    //table_html.slideDown("slow");
                }
                count = parseInt(tables[tables.length-1]);
                console.log(count);
                $(".count_free_num").html(count+"个座位空闲");
            }
           $(".screen-mask").addClass("none");
        },
        error: function(){
            bootbox.alert("<h1>请求失败</h1>", function() {
                this.hide();
                $(".screen-mask").addClass("none");
            });
        }
    });

     $.ajax({
        type:"POST",
        url:"http://www.myooms.com:8000/get_reservation/",
        data:datas,
        datatype: "html",//"xml", "html", "script", "json", "jsonp", "text".
        success:function(data){
            if(data=="False"){
                console.log("获取订单失败")
            }else{
                console.log(data);
                data = data.replace("\"","" );
                tables = data.split(",");
                reservations_container.html(" ");
                for(i=0;i<tables.length-1;i++){
                    table_num = parseInt(tables[i]);
                    console.log(table_num);
                    table_html = $('<div class="animated col-md-1 reservations meal-list table-list">' +
                            '<a style="color:white" target="_blank" href="http://www.myooms.com:8000/staff/book_table?id='+table_num+'">'+table_num+'号订单</a></div>');
                    reservations_container.append(table_html);
                    table_html.addClass(effects[RandomNum(0,5)]);
                }
                count = parseInt(tables[tables.length-1]);
                console.log(count);
                $(".count_reservations_num").html("这天有"+count+"个订单");
            }
        },
        error: function(){

        }
    });
}

function submit_suggestion() {

    name = $("input.name").val();
    suggestion = $("textarea.suggestion").val();
    connect_way = $("input.connect_way").val();
    like_or_unlike = $("input.like_or_unlike").val();
    datas = {"name":name, "suggestion":suggestion, "connect_way":connect_way, "like_or_unlike":like_or_unlike};
    console.log(datas);
    $.ajax({
        type:"POST",
        url:"suggestion/",
        data:datas,
        datatype: "html",//"xml", "html", "script", "json", "jsonp", "text".
        success:function(data){
            bootbox.alert(data, function() {
                this.hide();
                $(".screen-mask").addClass("none");
                window.location.href="http://www.myooms.com:8000";
            });
        },
        error: function(){
            bootbox.alert("<h1>error</h1>", function() {
                this.hide();
                $(".screen-mask").addClass("none");
            });
        }
    });
}

function export_excel(){
    $("div.screen-mask").removeClass("none");
    $.ajax({
        type:"GET",
        url:"export_excel/",
        datatype: "html",//"xml", "html", "script", "json", "jsonp", "text".
        success:function(data){
            bootbox.alert("<h1>导出表格成功</h1>", function() {
                this.hide();
                $(".screen-mask").addClass("none");
            });
        }   ,
        error: function(){
            bootbox.alert("<h1>导出表格出错</h1>", function() {
                this.hide();
                $(".screen-mask").addClass("none");
            });
        }
    });
}
