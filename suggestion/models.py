# -*- coding: utf-8 -*-
from django.db import models

class Suggestion(models.Model):
    like_or_dislike = models.CharField(verbose_name=u"喜欢与否", default=u"on", max_length=5)
    suggestion = models.TextField(verbose_name=u"建议", max_length=2000)
    published = models.DateTimeField(verbose_name=u"提交时间", auto_now_add=True)
    name = models.CharField(verbose_name=u"提交用户", max_length=200, null=True, blank=True)
    qq = models.CharField(verbose_name=u"联系方式", max_length=200, null=True, blank=True)

    class Meta:
        verbose_name = u"用户反馈"
        verbose_name_plural = u"用户反馈"
        ordering = ['-published']

    def __unicode__(self):
        return u"%s的反馈" % self.qq
