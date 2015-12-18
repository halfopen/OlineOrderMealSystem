# -*- coding: utf-8 -*-
__author__ = 'halfopen'

from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from models import *
from django.views.decorators.csrf import csrf_exempt
from restaurant.models import *
from datetime import timedelta
import urllib
import urllib2
import datetime
import xlwt


def index(req):
    if Table.objects.filter().exists():
            pass
    else:
        for i in range(1,20):
            table = Table(table_no=i, is_booked=False)
            table.save()

    return render_to_response("index.html", locals())


def about(req):
    return render_to_response("about.html", locals())


def author(req):
    return render_to_response("author.html", locals())


#
def export_excel(req):
    return True