# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Customer'
        db.create_table(u'restaurant_customer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('tel', self.gf('django.db.models.fields.IntegerField')(max_length=15)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
        ))
        db.send_create_signal(u'restaurant', ['Customer'])

        # Adding model 'Reservation'
        db.create_table(u'restaurant_reservation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('customer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['restaurant.Customer'])),
            ('number', self.gf('django.db.models.fields.IntegerField')(max_length=2)),
            ('year', self.gf('django.db.models.fields.IntegerField')(default=2015, max_length=6)),
            ('month', self.gf('django.db.models.fields.IntegerField')(default=1, max_length=6)),
            ('day', self.gf('django.db.models.fields.IntegerField')(default=1, max_length=2)),
            ('time', self.gf('django.db.models.fields.IntegerField')(default='moon', max_length=10)),
            ('is_valid', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('has_table', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'restaurant', ['Reservation'])

        # Adding model 'Table'
        db.create_table(u'restaurant_table', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('table_no', self.gf('django.db.models.fields.IntegerField')(unique=True, max_length=5)),
            ('is_booked', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('size', self.gf('django.db.models.fields.IntegerField')(default=8, max_length=2)),
            ('info', self.gf('django.db.models.fields.CharField')(default=u'xx\u9910\u5385\u7684xx\u697cxx\u4f4d\u7f6e\u5ea7\u4f4d', max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal(u'restaurant', ['Table'])

        # Adding M2M table for field reservation on 'Table'
        m2m_table_name = db.shorten_name(u'restaurant_table_reservation')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('table', models.ForeignKey(orm[u'restaurant.table'], null=False)),
            ('reservation', models.ForeignKey(orm[u'restaurant.reservation'], null=False))
        ))
        db.create_unique(m2m_table_name, ['table_id', 'reservation_id'])


    def backwards(self, orm):
        # Deleting model 'Customer'
        db.delete_table(u'restaurant_customer')

        # Deleting model 'Reservation'
        db.delete_table(u'restaurant_reservation')

        # Deleting model 'Table'
        db.delete_table(u'restaurant_table')

        # Removing M2M table for field reservation on 'Table'
        db.delete_table(db.shorten_name(u'restaurant_table_reservation'))


    models = {
        u'restaurant.customer': {
            'Meta': {'ordering': "['-name']", 'object_name': 'Customer'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'tel': ('django.db.models.fields.IntegerField', [], {'max_length': '15'})
        },
        u'restaurant.reservation': {
            'Meta': {'ordering': "['-is_valid']", 'object_name': 'Reservation'},
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