# -*- coding: utf-8 -*-
# Create your views here.
from models import Suggestion
from django.http import HttpResponse
from utils import render_json
from django.shortcuts import render_to_response
from django.core.mail import EmailMultiAlternatives


# 餐厅反馈
def suggestion(request):
    if not request.method == "POST":
        return render_to_response("suggestion.html", locals())
    try:
        like_or_unlike= request.REQUEST.get("like_or_unlike")
        user_suggestion = request.REQUEST.get("suggestion")
        qq = request.REQUEST.get("connect_way")
        if qq.__len__() > 200:
            return render_json("ToLong")


        number = request.REQUEST.get("name")
        new_suggestion = Suggestion()
        new_suggestion.like_or_dislike = like_or_unlike

        new_suggestion.number = number
        new_suggestion.suggestion = user_suggestion
        new_suggestion.qq = qq
        new_suggestion.save()

        subject,form_email,to = u'餐厅系统反馈', 'qinxiankang@gmail.com', '528397553@qq.com'
        text_content = 'This is an important message'
        html_content = u'姓名:' + number + u'<br />联系方式:'+ qq + u'<br />反馈内容:' + user_suggestion + u' <br />'
        html_content += u'<b>订餐系统</b><a href="http://www.myooms.com:8000">http:www.myooms.com</a>'
        msg = EmailMultiAlternatives(subject,text_content,form_email,[to])
        msg.attach_alternative(html_content, 'text/html')
        status = msg.send()


        return render_json("反馈状态:" + str(status))
    except:
        return render_json("NeedArgument")


