from django.db import models


class TimeFrameModel(models.Model):
    """ Generic time frame fields for all models """
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True