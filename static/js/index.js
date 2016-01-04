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
    $.ajax({
        type:"POST",
        url:"./",
        data:datas,
        datatype: "html",//"xml", "html", "script", "json", "jsonp", "text".
        success:function(data){
            if(data=="False"){
                bootbox.alert("<h1>False</h1>", function() {
                    this.hide();
                });
            }else{
                console.log(data);
                data = data.replace("\"","" );
                tables = data.split(",");
                table_container.html(" ");
                for(i=0;i<tables.length-1;i++){
                    table_num = parseInt(tables[i]);
                    console.log(table_num);

                    table_container.append('<div class="col-md-1 text-center meal-list table-list">' +
                            '<a style="color:white" href="../staff/table_detail?id='+table_num+'">'+table_num+'号桌子</a></div>'
                    );
                }
                count = parseInt(tables[tables.length-1]);
                console.log(count);
                $(".count_free_num").html(count+"个座位空闲");
            }
           $(".screen-mask").addClass("none");
        },
        error: function(){
            bootbox.alert("<h1>error</h1>", function() {
                this.hide();
                $(".screen-mask").addClass("none");
            });
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
