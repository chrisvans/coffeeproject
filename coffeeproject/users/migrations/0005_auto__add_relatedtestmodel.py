# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'RelatedTestModel'
        db.create_table(u'users_relatedtestmodel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('test_model', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['users.TestModel'])),
        ))
        db.send_create_signal(u'users', ['RelatedTestModel'])


    def backwards(self, orm):
        # Deleting model 'RelatedTestModel'
        db.delete_table(u'users_relatedtestmodel')


    models = {
        u'users.relatedtestmodel': {
            'Meta': {'object_name': 'RelatedTestModel'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'test_model': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['users.TestModel']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'users.testmodel': {
            'Meta': {'object_name': 'TestModel'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['users']