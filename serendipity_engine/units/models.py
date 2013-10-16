import logging

from django.db import models

logger = logging.getLogger(__name__)

class Unit(Unit):
    name = models.CharField(max_length=100)
    url = models.URLField(blank=True)
    
class Contributor(models.Model):
    name = models.CharField(max_length=100)
    contact_email = models.EmailField(blank=True)
    contact_phone = models.CharField(max_length=20, blank=True)