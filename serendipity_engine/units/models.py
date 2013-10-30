import logging

from django.db import models

logger = logging.getLogger(__name__)

class Unit(models.Model):
    class Meta:
        app_label = 'units'
        
    name = models.CharField(max_length=100)
    url = models.URLField(blank=True)
    
    def __unicode__(self):
        return u'%s' % self.name
        
class School(Unit):
    class Meta:
        app_label = 'units'
        
    subunits = models.ManyToManyField(Unit, related_name="schools")

class Contributor(models.Model):
    class Meta:
        app_label = 'units'
        
    name = models.CharField(max_length=100)
    contact_email = models.EmailField(blank=True)
    contact_phone = models.CharField(max_length=20, blank=True)
        
    def __unicode__(self):
        return u'%s' % self.name