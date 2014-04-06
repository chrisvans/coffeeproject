# Django
from django.db import models

# Python
import datetime
import pytz

class DoorTime(models.Model):

    active_time = models.DateTimeField(
        null=False, 
        default=datetime.datetime.utcnow().replace(tzinfo=pytz.UTC),
    )
    created = models.DateTimeField(auto_now_add=True)