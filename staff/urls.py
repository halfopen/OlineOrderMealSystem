# -*- coding:utf-8 -*-
__author__ = 'halfopen'

from django.conf.urls import *
from staff.views import *


urlpatterns = patterns(
    '',
    (r'^$', display_booking),
    (r'^display', display_booking),
    (r'^cancel', cancel_booking),
    (r'^add', add_booking),
    (r'^book_table', book_table),
    (r'^tables', show_tables),
    (r'^table_detail', table_detail),
)