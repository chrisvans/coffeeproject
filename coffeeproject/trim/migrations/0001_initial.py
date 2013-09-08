# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Trimurl'
        db.create_table(u'trim_trimurl', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('trimmed_url', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=500, blank=True)),
        ))
        db.send_create_signal(u'trim', ['Trimurl'])


    def backwards(self, orm):
        # Deleting model 'Trimurl'
        db.delete_table(u'trim_trimurl')


    models = {
        u'trim.trimurl': {
            'Meta': {'object_name': 'Trimurl'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'trimmed_url': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'})
        }
    }

    complete_apps = ['trim']