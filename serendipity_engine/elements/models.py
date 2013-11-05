from django.db import models

class Element(models.Model):
    """
    Records the parts of a project's tech stack, tools it relies on, etc.
    Examples: Django, Bootstrap, EAD, LCSH.
    """
    name = models.CharField(max_length=50)

    class Meta:
        app_label = 'elements'
        
    def __unicode__(self):
        return u'%s' % self.name
