import logging

from django.db import models

logger = logging.getLogger(__name__)

class Element(models.Model):
    name = models.CharField(max_length=50)
    
    def __unicode__(self):
        return u'%s' % self.name