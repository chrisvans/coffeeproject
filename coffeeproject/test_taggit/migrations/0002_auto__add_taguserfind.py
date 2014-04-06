# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TagUserFind'
        db.create_table(u'test_taggit_taguserfind', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'test_taggit', ['TagUserFind'])


    def backwards(self, orm):
        # Deleting model 'TagUserFind'
        db.delete_table(u'test_taggit_taguserfind')


    models = {
        u'test_taggit.food': {
            'Meta': {'object_name': 'Food'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'})
        },
        u'test_taggit.taguserfind': {
            'Meta': {'object_name': 'TagUserFind'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['test_taggit']