# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Suggestion'
        db.create_table(u'suggestion_suggestion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('like_or_dislike', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('suggestion', self.gf('django.db.models.fields.TextField')(max_length=2000)),
            ('published', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('student', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['zuosi.StudentNew'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('gender', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('number', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('academic', self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True)),
        ))
        db.send_create_signal(u'suggestion', ['Suggestion'])


    def backwards(self, orm):
        # Deleting model 'Suggestion'
        db.delete_table(u'suggestion_suggestion')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'suggestion.suggestion': {
            'Meta': {'ordering': "['-published']", 'object_name': 'Suggestion'},
            'academic': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'gender': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'like_or_dislike': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'published': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['zuosi.StudentNew']"}),
            'suggestion': ('django.db.models.fields.TextField', [], {'max_length': '2000'})
        },
        u'zuosi.academic': {
            'Meta': {'object_name': 'Academic'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'plane': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '1000'}),
            'plane_new': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '1000'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '500'})
        },
        u'zuosi.studentnew': {
            'Meta': {'object_name': 'StudentNew'},
            'academic': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['zuosi.Academic']", 'null': 'True', 'blank': 'True'}),
            'gender': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'hand_num': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'is_new': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_update': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "u'\\u672a\\u77e5'", 'max_length': '200'}),
            'other_course': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pwd': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'sing_in_date': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        }
    }

    complete_apps = ['suggestion']