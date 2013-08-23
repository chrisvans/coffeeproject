from django.db import models

from core.models import TimeStampedModel, ExtraModelMethods

class TestModel(TimeStampedModel, ExtraModelMethods):
    title = models.CharField(max_length=200)

