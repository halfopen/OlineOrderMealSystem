$(document).ready(function(){
  /* 弹出层 BEGIN */
  $("[data-toggle='popup']").click(function() {
    $($(this).attr("data-target")).fadeIn('slow');
    return false;
  });
  $("[data-toggle='close']").click(function() {
    $($(this).attr("data-target")).fadeOut('slow');
  });
  /* 弹出层 END */

  /* 用户反馈 BEGIN */
  $(".userreply .submit").click(function() {
    var fankui = $("input[name='fankui']:checked").val();
    if(!fankui) {
      $(".userreply span.hint").html('还没有选择一个选项呢');
      return false;
    }
    var suggestion = $(".userreply-suggestion").val();
    if(suggestion.length > 500) {
      $(".userreply span.hint").html('评论太长了！');
      return false;
    }
    var connectWay = $(".userreply-connactway").val();
    if(connectWay.length > 50) {
      $(".userreply span.hint").html('联系方式太长了！');
      return false;
    }
    $(".userreply .submit").html("提交中");
    $.ajax({
      type: 'post',
      url: '/suggestion/',
      dataType: 'json',
      data: {
        "like_or_unlike": fankui,
        "suggestion": suggestion,
        "connect_way": connectWay
      },
      error: function(XMLHttpRequest, textStatus) {
        $(".userreply-main span.hint").html('失败了呢，再试一次吧:(');
        $(".userreply-main .submit").html("确定");
      },
      success: function(data) { /* 提交成功 */
        if (data == "True") {
          $(".userreply-main").fadeOut(function() {
            $(".userreply-success").fadeIn();
            $(".userreply").delay(3000).fadeOut(function() {
              window.location.reload();
            });
          });
          $(".userreply-success span.hint").html('提交成功！感谢您的反馈，我们会做得更好~');
        }
        if (data == "NeedLogIn") {
          $(".userreply-main span.hint").html('你还没登录哦，现在去<a class="loginlink" href="/">登录</a>吧！');
        }
        $(".userreply-main .submit").html("确定");
      }
    })
    return false;
  })
  /* 用户反馈 END */

  /* IE8 hack BEGIN */

  var hack_list = [
    "#search-input",
    "#search-bar",
  ]
  for (var i = 0; i < hack_list.length; i ++) {
    if(window.PIE) {
      $(hack_list[i]).each(function() {
        PIE.attach(this);
      })
    }
  }

  /* IE8 hack END */


  $(".refresh").on("click", refresh);




});

function refresh(){
    location.reload() ;

}