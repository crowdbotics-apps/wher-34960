from django.conf import settings
from django.db import models


class Day(models.Model):
    "Generated Model"
    event1 = models.CharField(
        max_length=256,
    )
    event2 = models.CharField(
        max_length=256,
    )
    addEvent = models.BooleanField()
