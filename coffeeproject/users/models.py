from django.db import models
from django.contrib.auth.models import AbstractUser
from core.models import TimeStampedModel, ExtraModelMethods

class CoffeeUser(TimeStampedModel, ExtraModelMethods, AbstractUser):

    def __unicode__(self):
        return unicode(self.username + " " + self.email + " " + self.get_full_name())

    def get_bills(self):
        return self.bill_set.all()


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

