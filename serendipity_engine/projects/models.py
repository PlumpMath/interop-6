import logging

from django.db import models

from serendipity_engine.elements.models import Element
from serendipity_engine.project_types.models import ProjectType
from serendipity_engine.units.models import Unit, Contributor

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
    classlist = models.TextField(blank=True, null=True)
    
    def __unicode__(self):
        return u'%s' % self.name
        
    def save(self, *args, **kwargs):
        """
        In the navigation bar we need a list of css classes
        representing everything we might filter on for display.
        Easiest to generate it here, avoid having to do logic in the
        template.
        """
        classlist = ' '
        for unit in self.units.all():
            css_class = 'class_unit_' + str(unit.id) + ' '
            classlist += css_class
        for element in self.elements.all():
            css_class = 'class_element_' + str(element.id) + ' '
            classlist += css_class
        css_class = 'class_type_' + str(self.project_type.id)
        classlist += css_class
        self.classlist = classlist
        super(Project, self).save(*args, **kwargs)