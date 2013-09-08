from django.db import models
from core.models import TimeStampedModel, ExtraModelMethods

class Trimurl(TimeStampedModel, ExtraModelMethods):
    trimmed_url = models.CharField(max_length=100, blank=True)
    url = models.CharField(max_length=500, blank=True)

    def __unicode__(self):
        return unicode("Trim: " + self.trimmed_url + " - URL: " + self.url)
