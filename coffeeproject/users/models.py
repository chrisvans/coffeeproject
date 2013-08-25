from django.db import models

from core.models import TimeStampedModel, ExtraModelMethods

class TestModel(TimeStampedModel, ExtraModelMethods):
    title = models.CharField(max_length=200)

    def __unicode__(self):
    	return unicode(self.title)

