# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'TagUserFind'
        db.delete_table(u'test_taggit_taguserfind')

        # Deleting model 'Skills'
        db.delete_table(u'test_taggit_skills')

        # Deleting model 'Food'
        db.delete_table(u'test_taggit_food')

        # Deleting model 'LearnSkills'
        db.delete_table(u'test_taggit_learnskills')

        # Deleting model 'TeachSkills'
        db.delete_table(u'test_taggit_teachskills')


    def backwards(self, orm):
        # Adding model 'TagUserFind'
        db.create_table(u'test_taggit_taguserfind', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'test_taggit', ['TagUserFind'])

        # Adding model 'Skills'
        db.create_table(u'test_taggit_skills', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'test_taggit', ['Skills'])

        # Adding model 'Food'
        db.create_table(u'test_taggit_food', (
            ('teach', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['test_taggit.TeachSkills'])),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('learn', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['test_taggit.LearnSkills'])),
        ))
        db.send_create_signal(u'test_taggit', ['Food'])

        # Adding model 'LearnSkills'
        db.create_table(u'test_taggit_learnskills', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'test_taggit', ['LearnSkills'])

        # Adding model 'TeachSkills'
        db.create_table(u'test_taggit_teachskills', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'test_taggit', ['TeachSkills'])


    models = {
        
    }

    complete_apps = ['test_taggit']