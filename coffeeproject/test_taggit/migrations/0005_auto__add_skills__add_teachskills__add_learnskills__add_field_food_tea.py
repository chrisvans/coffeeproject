# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Skills'
        db.create_table(u'test_taggit_skills', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'test_taggit', ['Skills'])

        # Adding model 'TeachSkills'
        db.create_table(u'test_taggit_teachskills', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'test_taggit', ['TeachSkills'])

        # Adding model 'LearnSkills'
        db.create_table(u'test_taggit_learnskills', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'test_taggit', ['LearnSkills'])

        # Adding field 'Food.teach'
        db.add_column(u'test_taggit_food', 'teach',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['test_taggit.TeachSkills'], null=True),
                      keep_default=False)

        # Adding field 'Food.learn'
        db.add_column(u'test_taggit_food', 'learn',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['test_taggit.LearnSkills'], null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Skills'
        db.delete_table(u'test_taggit_skills')

        # Deleting model 'TeachSkills'
        db.delete_table(u'test_taggit_teachskills')

        # Deleting model 'LearnSkills'
        db.delete_table(u'test_taggit_learnskills')

        # Deleting field 'Food.teach'
        db.delete_column(u'test_taggit_food', 'teach_id')

        # Deleting field 'Food.learn'
        db.delete_column(u'test_taggit_food', 'learn_id')


    models = {
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'taggit.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'})
        },
        u'taggit.taggeditem': {
            'Meta': {'object_name': 'TaggedItem'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'taggit_taggeditem_tagged_items'", 'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'taggit_taggeditem_items'", 'to': u"orm['taggit.Tag']"})
        },
        u'test_taggit.food': {
            'Meta': {'object_name': 'Food'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'learn': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['test_taggit.LearnSkills']", 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'teach': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['test_taggit.TeachSkills']", 'null': 'True'})
        },
        u'test_taggit.learnskills': {
            'Meta': {'object_name': 'LearnSkills'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'test_taggit.skills': {
            'Meta': {'object_name': 'Skills'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'test_taggit.taguserfind': {
            'Meta': {'object_name': 'TagUserFind'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'test_taggit.teachskills': {
            'Meta': {'object_name': 'TeachSkills'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['test_taggit']