# -*- coding: utf-8 -*-
__author__ = 'halfopen'

from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from models import *
from django.views.decorators.csrf import csrf_exempt
from restaurant.models import *
from utils import render_json
from datetime import timedelta
import urllib
import urllib2
import datetime
import xlwt
import json

def index(req):
    if Table.objects.filter().exists():
            pass
    else:
        for i in range(1,21):
            table = Table(table_no=i, is_booked=False)
            table.save()

    return render_to_response("index.html", locals())


def about(req):
    return render_to_response("about.html", locals())


def author(req):
    return render_to_response("author.html", locals())


#
def export_excel(req):
    try:
        wb = xlwt.Workbook(encoding='utf-8')
        sheet1 = wb.add_sheet("Tables")
        sheet2 = wb.add_sheet("Orders")

        tables = Table.objects.filter()
        reservations = Reservation.objects.filter().order_by('year')

        sheet1.write(0, 0, u"编号")
        sheet1.write(0, 1, u"容量")
        sheet1.write(0, 2, u"信息")
        i = 1
        for t in tables:
            sheet1.write(i, 0, t.table_no)
            sheet1.write(i, 1, t.size)
            sheet1.write(i, 2, t.info)
            i += 1

        sheet2.write(0, 0, u"名字")
        sheet2.write(0, 1, u"年")
        sheet2.write(0, 2, u"月")
        sheet2.write(0, 3, u"日")
        sheet2.write(0, 4, u"时间段")
        sheet2.write(0, 5, u"手机号")
        sheet2.write(0, 6, u"人数")
        i = 1
        for r in reservations:
            sheet2.write(i, 0, r.customer.name)
            sheet2.write(i, 1, r.year)
            sheet2.write(i, 2, r.month)
            sheet2.write(i, 3, r.day)
            sheet2.write(i, 4, str(r.time)+u":00")
            sheet2.write(i, 5, r.customer.tel)
            sheet2.write(i, 6, r.number)
            i += 1

        # wb.save("OOMS.xls")
        response = HttpResponse(content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename=OOMS'+str(datetime.datetime.now())+'.xls'

        wb.save(response)
        return response
    except:
        return False #


#
def free_table(req):
    tables = ""
    if req.method == "POST":
        if req.POST.has_key("date") and req.POST.has_key("time"):
            try:
                date_str = req.POST["date"]
                time = req.POST["time"]
                dic = date_str.split("-")
                year = dic[0]
                month = dic[1]
                day = dic[2]
                count = 0
                tables_set = Table.objects.exclude(reservation=None)
                for t in tables_set:
                    if t.reservation.filter(year=year, month=month, day=day, time=time, is_valid=True).exists():
                        continue
                    else:
                        tables+=str(t.table_no)+","
                        count += t.size
                tables+=str(count)
                # print json.dumps(tables)
                return HttpResponse(json.dumps(tables))
            except:
                return render_json("False")
    info = "free tables"
    return render_to_response("free_table.html", locals())