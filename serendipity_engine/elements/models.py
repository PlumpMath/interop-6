from django.db import models

class Element(models.Model):
    """
    Parts of a project's tech stack, tools it relies on, etc.
    Examples: Django, Bootstrap, EAD, LCSH.
    """
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return u'%s' % self.name
