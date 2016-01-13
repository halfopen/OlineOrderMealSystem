$(document).ready(function(){

    $('.selectpicker').selectpicker({
  style: 'btn-info',
  size: 4
});

  $(".refresh").on("click", refresh);


  $(".row a").click(function(){
        var _this = $(this);
        //$("div.index-guide").css("display","none");
        //$("div.index-guide").addClass("Selected-guide");
         //$(this).parent().addClass("animated");

        $(this).parent().addClass("flip");
       // $(this).parents(".index-guide").css("display","block");
//        $(".Selected-guide").slideUp(2000, function() {
//                this.remove();
//            });
       //$(".Selected-guide").remove();
     // alert(1);
        window.location.href = _this.attr("href");
        return false;
    });

    $("div.row-content").mouseenter(function(){
        $(this).removeClass("swing");
        $(this).addClass("pulse");
    });

    $("div.row-content").mouseleave(function(){
        $(this).removeClass("swing");
        $(this).removeClass("pulse");
    });
});

function refresh(){
    location.reload() ;

}

function RandomNum(Min,Max){
    var Range = Max - Min;
    var Rand = Math.random();
    var num = Min + Math.round(Rand * Range);
    return num;
}