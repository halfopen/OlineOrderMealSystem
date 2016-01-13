# -*- coding: utf-8 -*-
# Create your views here.

from models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from utils import render_json
from restaurant.models import *
from django.core.exceptions import ObjectDoesNotExist

WEB_INDEX = "http://www.myooms.com:8000"


# 首页
def index(req):
    return render_to_response("staff/index.html", locals())


# 显示所有桌子
def display_booking(req):
    reservations = Reservation.objects.filter(is_valid=True).order_by('-pk').order_by("-is_valid")
    return render_to_response("staff/index.html", locals())


# 显示所有桌子
def show_tables(req):
    tables = Table.objects.filter()
    #print tables
    return render_to_response("staff/table.html", locals())


# 重置桌子状态
def reset_table(req):
    if req.GET.has_key("id"):
        t_id = req.GET["id"]
        try:
            table = Table.objects.get(pk=t_id)
            table.reset()
        except ObjectDoesNotExist:
            info = u"桌子不存在"
            return HttpResponseRedirect(WEB_INDEX)
    else:
        return HttpResponseRedirect(WEB_INDEX+"/staff")


# 显示桌子详情
def table_detail(req):
    if req.GET.has_key("id"):
        t_id = req.GET["id"]
        try:
            table = Table.objects.get(pk=t_id)
            reservations = table.reservation.filter(is_valid=True)
            print reservations
        except ObjectDoesNotExist:
            info = u"桌子不存在"
            return HttpResponseRedirect(WEB_INDEX+"/staff")
        return render_to_response("staff/table_detail.html", locals())
    else:
        return HttpResponseRedirect(WEB_INDEX+"/staff")


# 取消
def cancel_booking(req):
    dict = {}
    info = 'Data log save success'
    try:
        if req.POST.has_key('id'):
            r_id = req.POST['id']
            reservation = Reservation.objects.get(id=r_id)
        else:
            return render_json("False")
    except ObjectDoesNotExist:
        return render_json("False")

    tables = Table.objects.filter(reservation=reservation)
    for t in tables:
        t.reset()
    reservation.is_valid = False
    reservation.save()
    return render_json("True")


# 添加订单
def add_booking(req):
    if req.method == "POST":
        try:
            print req.POST
            name = req.REQUEST.get("name")
            tel = req.REQUEST.get("tel")
            number = req.REQUEST.get("number")
            date = req.REQUEST.get("date")
            dic = date.split("-")
            year = dic[0]
            month = dic[1]
            day = dic[2]
            time = req.REQUEST.get("time")
            try:
                customer = Customer.objects.get(name=name, tel=tel)
                print customer
            except ObjectDoesNotExist:
                print "create new customer\n"
                try:
                    customer = Customer(name=name, tel=tel)
                    customer.save()
                    print customer
                except:
                    info = u"新建客户失败，是否手机号已经被占用？"
                    return render_to_response("staff/add.html", locals())
                info = u"新建用户"
            reservation = Reservation(customer=customer, number=number,time=time, year=year, month=month, day=day, is_valid=True)
            reservation.save()
            info = u"添加成功！"
            return HttpResponseRedirect(WEB_INDEX+"/staff")
        except:
            info = u"请输入相关信息进行预订"
            print info
            return render_to_response("staff/add.html", locals())
    else:
        # print "GET"
        info = u"请添加订单"
    return render_to_response("staff/add.html", locals())


# 分配桌子
def book_table(req):
    valid_tables = []
    invalid_tables = []
    my_tables =[]
    reservation_id = 0
    # 显示桌子
    if req.method == "GET":
        try:
            reservation_id = req.REQUEST.get("id")
            reservation = Reservation.objects.get(pk=reservation_id)
            print reservation_id
            tables = Table.objects.filter() # 得到所有桌子

            for t in tables:
                #print t.reservation.filter(is_valid=True)
                #print (t.reservation.filter(is_valid=True) is None)
                if not t.reservation.filter(is_valid=True):
                    valid_tables.append(t)
                elif t.reservation.filter(year=reservation.year, month=reservation.month, day=reservation.day, time=reservation.time).exists():
                    if t.reservation.filter(pk=reservation_id).exists():
                        my_tables.append(t)
                    else:
                        invalid_tables.append(t)
                else:
                    valid_tables.append(t)
            print reservation_id

            return render_to_response("staff/book_table.html", locals())
        except :
            return HttpResponseRedirect('../')

    # 处理Post请求
    try:
        reservation_id = req.REQUEST.get("r_id")
        try:
            reservation = Reservation.objects.get(pk=reservation_id)
        except ObjectDoesNotExist:
            return render_json("Reservation_id error")
        tables_str = req.REQUEST.get("tables_id")
        tables = []
        i = 0
        for t in tables_str.split("-"):
            i += 1
            if i == 1:
                continue
            tables.append(t)

        # 清除之前桌子
        former_tables = Table.objects.filter(reservation=reservation)
        for t in former_tables:
            t.reservation.remove(reservation)

        # 遍历桌子
        for i in tables:
            try:
                t = Table.objects.get(pk=i)
                if not t.book_table(reservation_id): # 如果预定失败
                    return render_json(u"预约桌子"+str(t.table_no)+u"失败")
                else:
                    try:
                        t.reservation.add(reservation)
                    except:
                        print u"添加预约失败"
                        return render_json(u"添加预约失败")
                    t.save()
            except ObjectDoesNotExist:
                pass
        reservation.has_table = True
        reservation.save()
    except:
        render_json("False")
    return render_json("True")




