from django.db import models
from .timeframe import TimeFrameModel
from .publisher import Publisher
from .author import Author


class Book(TimeFrameModel, models.Model):
    """ Books model """
    name = models.CharField(max_length=250)
    author = models.ForeignKey(Author, 
                                on_delete=models.CASCADE,
                                related_name='author')
    publisher = models.ForeignKey(Publisher,
                                    on_delete=models.CASCADE,
                                    related_name='publisher')
    slug = models.SlugField(unique=True, editable=False)

    def __str__(self):
        return self.name
    