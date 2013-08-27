from django.db import models
from core.models import TimeStampedModel, ExtraModelMethods

class Bill(TimeStampedModel, ExtraModelMethods):
    title = models.CharField(max_length=200)
    user = models.ForeignKey('users.CoffeeUser')

    def __unicode__(self):
        return unicode(self.title)