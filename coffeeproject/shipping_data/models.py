from django.db import models
from core.models import TimeStampedModel, ExtraModelMethods

class ShippingAddress(TimeStampedModel, ExtraModelMethods):
    pass