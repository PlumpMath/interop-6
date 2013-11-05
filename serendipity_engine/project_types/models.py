import logging

from django.db import models

logger = logging.getLogger(__name__)

class ProjectType(models.Model):
    name = models.CharField(max_length=50,
                    help_text="Plural noun (e.g. 'Collections'), for display")
    description = models.TextField()
    
    class Meta:
        app_label = 'project_types'
        
    def __unicode__(self):
        return u'%s' % self.name