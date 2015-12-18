# -*- coding: utf-8 -*-
import time
import requests
from django.db import models
from django.contrib.auth.models import User


class Staff(models.Model):
    name = models.CharField(max_length=200, null=False, unique=True, verbose_name=u"姓名")

    class Meta:
        verbose_name = u"员工"
        verbose_name_plural = u"员工"
        #ordering = ['-']

    def __unicode__(self):
        return u"%s" % self.name


class ReceptionList(models.Model):
    user = models.ForeignKey(Staff)

    class Meta:
        verbose_name = u"接待员"
        verbose_name_plural = u"接待员"
        #ordering = ['-']

    def __unicode__(self):
        return u"接待员:%s" % self.user.name

    def record_booking(self):
        pass

    def record_arrival(self):
        pass

    def cancel_booking(self):
        pass

    def change_table(self):
        pass


class HeadWaiter(models.Model):
    user = models.ForeignKey(Staff)

    class Meta:
        verbose_name = u"领班"
        verbose_name_plural = u"领班"
        #ordering = ['-']

    def __unicode__(self):
        return u"领班:%s" % self.user.name