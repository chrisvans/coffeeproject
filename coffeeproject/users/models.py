from django.db import models
from django.contrib.auth.models import AbstractUser
from core.models import TimeStampedModel, ExtraModelMethods

class CoffeeUser(TimeStampedModel, ExtraModelMethods, AbstractUser):

    def __unicode__(self):
        return unicode(self.username + " " + self.email + " " + self.get_full_name())

    def get_bills(self):
        return self.bill_set.all()
