import logging

from django.db import models

logger = logging.getLogger(__name__)

class BaseUnit(models.Model):
    """
    Provides elements common to Schools and Units. Is abstract to ensure
    that elements cannot belong to both classes; the overlapping primary
    keys would confuse the Unit detailview.
    """
    name = models.CharField(max_length=100)
    url = models.URLField(blank=True)

    class Meta:
        abstract = True
        app_label = 'units'
        
class Unit(BaseUnit):            
    class Meta:
        app_label = 'units'

    def __unicode__(self):
        return u'%s' % self.name
        
class School(BaseUnit):
    subunits = models.ManyToManyField(Unit, related_name="schools")

    class Meta:
        app_label = 'units'
        
class Contributor(models.Model):
    name = models.CharField(max_length=100)
    contact_email = models.EmailField(blank=True)
    contact_phone = models.CharField(max_length=20, blank=True)

    class Meta:
        app_label = 'units'
        
    def __unicode__(self):
        return u'%s' % self.name
