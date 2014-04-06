# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Food'
        db.delete_table(u'test_taggit_food')


    def backwards(self, orm):
        # Adding model 'Food'
        db.create_table(u'test_taggit_food', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
        ))
        db.send_create_signal(u'test_taggit', ['Food'])


    models = {
        u'test_taggit.taguserfind': {
            'Meta': {'object_name': 'TagUserFind'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['test_taggit']