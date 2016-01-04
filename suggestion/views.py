# -*- coding: utf-8 -*-
# Create your views here.
from models import Suggestion
from django.http import HttpResponse
from utils import render_json
from django.shortcuts import render_to_response


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
        return render_json("ok")
    except:
        return render_json("NeedArgument")


