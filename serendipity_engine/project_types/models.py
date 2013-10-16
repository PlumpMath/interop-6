import logging

from django.db import models

logger = logging.getLogger(__name__)

class Type(models.Model):
    name = models.CharField(max_length=50,
                    help_text="Plural noun (e.g. 'Collections'), for display")
    description = models.TextField()