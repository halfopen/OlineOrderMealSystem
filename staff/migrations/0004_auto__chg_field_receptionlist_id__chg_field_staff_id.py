# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'ReceptionList.id'
        db.alter_column(u'staff_receptionlist', u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True))

        # Changing field 'Staff.id'
        db.alter_column(u'staff_staff', u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True))

    def backwards(self, orm):

        # Changing field 'ReceptionList.id'
        db.alter_column(u'staff_receptionlist', 'id', self.gf('django.db.models.fields.IntegerField')(primary_key=True))

        # Changing field 'Staff.id'
        db.alter_column(u'staff_staff', 'id', self.gf('django.db.models.fields.IntegerField')(primary_key=True))

    models = {
        u'staff.headwaiter': {
            'Meta': {'object_name': 'HeadWaiter'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['staff.Staff']"})
        },
        u'staff.receptionlist': {
            'Meta': {'object_name': 'ReceptionList'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['staff.Staff']"})
        },
        u'staff.staff': {
            'Meta': {'object_name': 'Staff'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'})
        }
    }

    complete_apps = ['staff']