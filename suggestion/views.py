# -*- coding: utf-8 -*-
# Create your views here.
from form import SuggestionForm
from models import Suggestion
from django.http import HttpResponse
from utils import render_json
from django.shortcuts import render_to_response


def suggestion(request):
    if not request.user.is_authenticated():
        return render_json("NeedLogIn")

    if not request.method == "POST":
        return render_to_response("suggestion.html", locals())
    form = SuggestionForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        like_or_unlike = cd["like_or_unlike"]
        user_suggestion = cd["suggestion"]
        qq = cd["connect_way"]
        if qq.__len__() > 200:
            return render_json("ToLong")


        number = request.user.username
        new_suggestion = Suggestion()
        new_suggestion.like_or_dislike = like_or_unlike

        new_suggestion.number = number
        new_suggestion.suggestion = user_suggestion
        new_suggestion.qq = qq
        new_suggestion.save()
        return render_json("True")
    else:
        return render_json("NeedArgument")


