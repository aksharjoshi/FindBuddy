# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Traveller(models.Model):
    name = models.CharField(max_length=140)
    number = models.IntegerField()
    travel_start_date = models.DateTimeField()
    travel_end_date = models.DateTimeField()
    country = models.CharField(max_length=20)

    def __str__(self):
        return self.name