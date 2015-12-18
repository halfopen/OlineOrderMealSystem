# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Customer'
        db.delete_table(u'staff_customer')


    def backwards(self, orm):
        # Adding model 'Customer'
        db.create_table(u'staff_customer', (
            ('name', self.gf('django.db.models.fields.CharField')(default=u'\u672a\u77e5', max_length=200)),
            ('gender', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('pwd', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'staff', ['Customer'])


    models = {
        u'staff.headwaiter': {
            'Meta': {'object_name': 'HeadWaiter'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['staff.Staff']"})
        },
        u'staff.receptionlist': {
            'Meta': {'object_name': 'Receptionlist'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['staff.Staff']"})
        },
        u'staff.staff': {
            'Meta': {'object_name': 'Staff'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['staff']