# -*- coding: utf-8 -*-
__author__ = 'halfopen'
from models import *
from django.contrib import admin


class TableAdmin(admin.ModelAdmin):
    list_display=('table_no', 'size', 'info', 'is_booked')   # 列表显示
    list_filter = ('size',)             # 过滤器
class ReservationAdmin(admin.ModelAdmin):
    list_display=('customer', 'number', 'year', 'month', 'day', 'time', 'has_table', 'is_valid')   # 列表显示


class CustomerAdmin(admin.ModelAdmin):
    list_display=('name', 'tel')   # 列表显示
    search_fields = ('name',)

admin.site.register(Reservation, ReservationAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Table,TableAdmin)