from django.db import models

from django_model_shortcuts.models import TimeStampedModel, ExtraModelMethods

class TestModel(TimeStampedModel, ExtraModelMethods):
    title = models.CharField(max_length=200)

