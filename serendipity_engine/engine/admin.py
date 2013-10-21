from django.contrib import admin
from django.core.urlresolvers import reverse

from elements.models import Element
from project_types.models import ProjectType
from projects.models import Project
from units.models import Unit, Contributor

class ElementAdmin(admin.ModelAdmin):
    list_display = ('name',)
      
admin.site.register(Element, ElementAdmin)


class ProjectTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    #fields = ('name', 'description')
      
admin.site.register(ProjectType, ProjectTypeAdmin)


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'project_type')
    fields = ('name', 'description', 'contact_email', 'contact_phone',
              'office_location', 'units', 'url', 'contributors', 
              'status', 'start_date', 'end_date', 'elements',
              'project_type')
    
admin.site.register(Project, ProjectAdmin)


class UnitAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')
 
admin.site.register(Unit, UnitAdmin)


class ContributorAdmin(admin.ModelAdmin):
    list_display = ('name',)
 
admin.site.register(Contributor, ContributorAdmin)