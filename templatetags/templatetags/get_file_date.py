# -*- coding: utf-8 -*-
__author__ = 'fuxiuyin'
from django import template
from OOMS.settings import ROOT_PATH
import commands

register = template.Library()


def get_file_date(text):
    file_path = u"%s/%s" % (ROOT_PATH, text)
    commend = u"date -r %s +%s" % (file_path, r"%s")
    status, result = commands.getstatusoutput(commend)
    return u"%s?date=%s" % (text, result)

register.filter('get_file_date', get_file_date)
