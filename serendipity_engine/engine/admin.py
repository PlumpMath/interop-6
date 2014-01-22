from django.contrib import admin

from serendipity_engine.elements.models import Element
from serendipity_engine.project_types.models import ProjectType
from serendipity_engine.projects.models import Project
from serendipity_engine.units.models import Unit, Contributor, School

class ElementAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')

admin.site.register(Element, ElementAdmin)


class ProjectTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')

admin.site.register(ProjectType, ProjectTypeAdmin)


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('display_name', 'name', 'url', 'project_type')
    fields = ('display_name', 'name', 'description', 'contact_email',
              'contact_phone', 'units', 'url', 'contributors', 'status', 
              'start_date', 'end_date', 'elements', 'project_type',
              'projects_interoperated_with')

admin.site.register(Project, ProjectAdmin)


class UnitAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'id')

admin.site.register(Unit, UnitAdmin)
admin.site.register(School, UnitAdmin)


class ContributorAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')

admin.site.register(Contributor, ContributorAdmin)
