from django.db import models
from .timeframe import TimeFrameModel


class Publisher(TimeFrameModel, models.Model):
    """ Model for Publisher """
    name = models.CharField(max_length=250)
    active = models.BooleanField(default=True)
    slug = models.SlugField(unique=True, editable=False)

    def __str__(self):
        return self.name
    