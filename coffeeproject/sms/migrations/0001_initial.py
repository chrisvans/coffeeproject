# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'DoorTime'
        db.create_table(u'sms_doortime', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('active_time', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 4, 6, 0, 0))),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'sms', ['DoorTime'])


    def backwards(self, orm):
        # Deleting model 'DoorTime'
        db.delete_table(u'sms_doortime')


    models = {
        u'sms.doortime': {
            'Meta': {'object_name': 'DoorTime'},
            'active_time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 4, 6, 0, 0)'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['sms']