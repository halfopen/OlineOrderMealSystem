# -*- coding: utf-8 -*-
__author__ = 'fuxiuyin'
from django import forms


class SuggestionForm(forms.Form):
    like_or_unlike = forms.IntegerField(label=u"顶或踩")
    suggestion = forms.CharField()
    connect_way = forms.CharField(required=False)

    def clean_like_or_unlike(self):
        like_or_unlike = int(self.cleaned_data.get("like_or_unlike", None))
        if like_or_unlike is None:
            raise forms.ValidationError(u"请选择")
        if not like_or_unlike == 0 and not like_or_unlike == 1:
            raise forms.ValidationError(u"为知错误")
        return like_or_unlike

    def clean_suggestion(self):
        suggest = self.cleaned_data.get("suggestion", None)
        if not suggest:
            raise forms.ValidationError(u"请填写建议")
        if suggest.__len__() > 500:
            raise forms.ValidationError(u"建议请少于500字")
        return suggest
