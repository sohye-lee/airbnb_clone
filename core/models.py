from django.db import models


class TimeStampedModel(models.Model):

    """ TIME STAMPED MODEL DEFINITION"""

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ### MODEL NOT GOING TO THE DATABASE ###
        abstract = True 