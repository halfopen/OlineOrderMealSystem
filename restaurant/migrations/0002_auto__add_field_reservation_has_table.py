# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Reservation.has_table'
        db.add_column(u'restaurant_reservation', 'has_table',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Reservation.has_table'
        db.delete_column(u'restaurant_reservation', 'has_table')


    models = {
        u'restaurant.customer': {
            'Meta': {'ordering': "['-name']", 'object_name': 'Customer'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'tel': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'max_length': '15'})
        },
        u'restaurant.reservation': {
            'Meta': {'object_name': 'Reservation'},
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['restaurant.Customer']"}),
            'day': ('django.db.models.fields.IntegerField', [], {'default': '1', 'max_length': '2'}),
            'has_table': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_valid': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'month': ('django.db.models.fields.IntegerField', [], {'default': '1', 'max_length': '6'}),
            'number': ('django.db.models.fields.IntegerField', [], {'max_length': '2'}),
            'time': ('django.db.models.fields.IntegerField', [], {'default': "'moon'", 'max_length': '10'}),
            'year': ('django.db.models.fields.IntegerField', [], {'default': '2015', 'max_length': '6'})
        },
        u'restaurant.table': {
            'Meta': {'ordering': "['table_no']", 'object_name': 'Table'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.CharField', [], {'default': "u'xx\\u9910\\u5385\\u7684xx\\u697cxx\\u4f4d\\u7f6e\\u5ea7\\u4f4d'", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'is_booked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'reservation': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['restaurant.Reservation']", 'null': 'True', 'blank': 'True'}),
            'size': ('django.db.models.fields.IntegerField', [], {'default': '8', 'max_length': '2'}),
            'table_no': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'max_length': '5'})
        }
    }

    complete_apps = ['restaurant']