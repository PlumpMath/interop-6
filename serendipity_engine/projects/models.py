import logging

from django.db import models

from serendipity_engine.elements.models import Element
from serendipity_engine.project_types.models import ProjectType
from serendipity_engine.units.models import Unit, Contributor, School

logger = logging.getLogger(__name__)

class Project(models.Model):
    class Meta:
        app_label = 'projects'
        
    name = models.CharField(max_length=100)
    short_description = models.CharField(max_length=140,
        help_text="Tweet-length (140 chars) description of the project for "
        "its display tile")
    description = models.TextField(blank=True, null=True,
        help_text="Description of the project")
    contact_email = models.EmailField(blank=True)
    contact_phone = models.CharField(max_length=20, blank=True)
    units = models.ManyToManyField(Unit, blank=True, 
        related_name="projects",
        verbose_name="Group(s)",
        help_text="Group(s) with primary responsibility for the project")
    school = models.ManyToManyField(School, blank=True,
        help_text="Harvard unit(s) within which the group resides")
    url = models.URLField(blank=True, help_text="Project's home page")
    contributors = models.ManyToManyField(Contributor, 
        blank=True, related_name="projects")
    status = models.CharField(max_length=100, blank=True,
        help_text="Current status of the project")
    start_date = models.DateField(blank=True, null=True,
        help_text="When did it start?")
    end_date = models.DateField(blank=True, null=True,
        help_text="When is it supposed to end?")
    elements = models.ManyToManyField(Element, blank=True, 
        related_name="projects", verbose_name="Building blocks",
        help_text="Functional elements of the project, including technology, "
        "schema, ontologies, collections, standards supported, etc.")
    project_type = models.ForeignKey(ProjectType, blank=True, null=True, 
        related_name="projects")
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
        # must exist before we can follow db relationships
        super(Project, self).save(*args, **kwargs) 
        classlist = ' '
        for unit in self.units.all():
            css_class = 'class_unit_' + str(unit.id) + ' '
            classlist += css_class
        for element in self.elements.all():
            css_class = 'class_element_' + str(element.id) + ' '
            classlist += css_class
        if self.project_type:
            css_class = 'class_type_' + str(self.project_type.id)
            classlist += css_class
        self.classlist = classlist
        # and save our changes
        super(Project, self).save(*args, **kwargs)
