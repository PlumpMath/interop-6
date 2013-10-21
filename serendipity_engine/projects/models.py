import logging

from django.db import models

from elements.models import Element
from project_types.models import ProjectType
from units.models import Unit, Contributor

logger = logging.getLogger(__name__)

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    contact_email = models.EmailField(blank=True)
    contact_phone = models.CharField(max_length=20, blank=True)
    office_location = models.CharField(max_length=100, blank=True)
    units = models.ManyToManyField(Unit, blank=True, related_name="projects")
    url = models.URLField(blank=True)
    contributors = models.ManyToManyField(Contributor, blank=True)
    status = models.CharField(max_length=100, blank=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    elements = models.ManyToManyField(Element, blank=True, related_name="projects")
    project_type = models.ForeignKey(ProjectType, blank=True, null=True, related_name="projects")
    
    
    def __unicode__(self):
        return u'%s' % self.name