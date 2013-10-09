import logging

from django.db import models

logger = logging.getLogger(__name__)

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    contact_email = models.EmailField(blank=True)
    contact_phone = models.CharField(max_length=20, blank=True)
    office_location = models.CharField(max_length=100, blank=True)
    unit = models.ManyToManyField(Unit, blank=True)
    url = models.URLField(blank=True)
    contributors = models.ManyToManyField(blank=True)
    status = models.CharField(max_length=100, blank=True)
    start_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True)
    elements = models.ManyToManyField(blank=True)