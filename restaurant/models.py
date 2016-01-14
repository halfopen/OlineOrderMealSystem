# -*- coding: utf-8 -*-
__author__ = 'halfopen'
from django.db import models


# 客户
class Customer(models.Model):
    name = models.CharField(verbose_name=u'姓名', max_length=200, null=False)
    tel = models.IntegerField(verbose_name=u'电话', max_length=15, null=False, unique=True)
    # email = models.EmailField(verbose_name=u'邮箱')

    class Meta:
        verbose_name = u"客户"
        verbose_name_plural = u"客户"
        ordering = ['-name']

    def __unicode__(self):
        return u"姓名:%s 手机:%s" % (self.name, self.tel)


# 订餐
class Reservation(models.Model):
    customer = models.ForeignKey(Customer, verbose_name=u"订餐用户", null=False)
    number = models.IntegerField(verbose_name=u'人数', max_length=2, null=False)
    year = models.IntegerField(verbose_name=u"年", max_length=6, default=2015)
    month = models.IntegerField(verbose_name=u"月", default=1, null=False, blank=False, max_length=6,
        choices=( (1,u"1月"), (2, u"2月"), (3, u"3月"),
        (4, u"4月"), (5, u"5月"), (6, u"6月"), (7, u"7月"), (8, u"8月"), (9, u"9月"), (10,u"10月"), (11, u"11月"), (12, u"12月")))
    day = models.IntegerField(max_length=2, default=1, null=False, blank=False, choices=((1,u"1号"), (2,u"2号"),(1, "1号")
        , (2, "2号"), (3, "3号"),(4, "4号"),(5, "5号"),(6, "6号"),(7, "7号"),(8, "8号"),(9, "9号"),(10, "10号")
        , (11, "11号"), (12, "12号"),(13, "13号"),(14, "14号"),(15 ,"15号"),(16, "16号"),(17, "17号"),(18, "18号")
        , (19, "19号"), (20, "20号"),(21, "21号"),(22, "22号"),(23, "23号"),(24, "24号"),(25, "25号"),(26, "26号")
        , (27, "27号"), (28, "28号"),(29, "29号"),(30, "30号"),(31, "31号")))
    time = models.IntegerField(verbose_name=u"时间段", default="moon", null=False, blank=False,
        choices=((9, u"早上"), (12, u"上午"), (15, u"下午"), (18, u"晚上")), max_length = 10)
    is_valid = models.BooleanField(verbose_name=u"是否有效", default=True, blank=False, null=False)
    has_table = models.BooleanField(verbose_name=u"是否已经分配桌子", default=False)

    class Meta:
        verbose_name = u"订单"
        verbose_name_plural = u"订单"
        ordering = ['-is_valid']

    def __unicode__(self):
        # date = str(self.year)+u" - "+str(self.month)+str(self.day)+str(self.time)
        date = u" "
        if self.is_valid:
            return u"%s %d人在%s的订单" % (self.customer,self.number,date)
        else:
            return u"无效订单:%s %d人在%s的订单" % (self.customer,self.number, date)

    # 检查订单是否过期(应该结账的时候手动添加)
    def check_valid(self):
        pass


# 桌子
class Table(models.Model):
    table_no = models.IntegerField(max_length=5, null=False, unique=True, verbose_name=u"桌位号")
    is_booked = models.BooleanField(verbose_name=u"是否有人预定")
    size = models.IntegerField(max_length=2, verbose_name=u"可容纳人数", default=8)
    reservation = models.ManyToManyField(Reservation, verbose_name=u"已有订单", null=True, blank=True)
    info = models.CharField(max_length=200, verbose_name=u"座位信息", null=True, blank=True, default=u"xx餐厅的xx楼xx位置座位")

    class Meta:
        verbose_name = u"桌位"
        verbose_name_plural = u"桌位"
        ordering = ['table_no']

    def __unicode__(self):
        if self.is_booked:
            return u"%03d 号桌，可容纳%d人" % (self.table_no, self.size)
        else:
            return u"%03d 号桌，可容纳%d人，空闲" % (self.table_no, self.size)

    # 重置桌子状态
    def reset(self):
        self.is_booked = False
        self.reservation.remove()
        print u"清空订单"
        self.save()

    # 预定桌子
    def book_table(self, reservation_id):
        rsv = Reservation.objects.get(pk=reservation_id)
        if rsv is None:
            return False
        self.reservation.add(rsv)
        self.is_booked = True
        self.save()
        return True

    # 去除无效订单
    def remove_invalid(self):
        invalid_rsv = Reservation.objects.filter(is_valid=False)
        for i in invalid_rsv:
            self.reservation.remove(i)
        self.save()