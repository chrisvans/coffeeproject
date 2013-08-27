from django.db import models

from core.models import TimeStampedModel, ExtraModelMethods

class TestModel(TimeStampedModel, ExtraModelMethods):
    title = models.CharField(max_length=200)

    def __unicode__(self):
        return unicode(self.title)

    def get_bills(self):
        return self.relatedtestmodel_set.all()

class RelatedTestModel(TimeStampedModel, ExtraModelMethods):
    title = models.CharField(max_length=200)
    test_model = models.ForeignKey('TestModel')

    def __unicode__(self):
        return unicode(self.title)

