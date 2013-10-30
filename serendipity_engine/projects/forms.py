from django import forms

import autocomplete_light

from .models import Project
from serendipity_engine.units.models import Unit

class ProjectForm(autocomplete_light.FixedModelForm):
    add_new_elements = forms.CharField(max_length=100, required=False,
        help_text="If your project uses building blocks that aren't "
        "already in the database, you can add a comma-separated list "
        "here.")
        
    add_new_groups = forms.CharField(max_length=100, required=False,
        help_text="If your project belongs to Harvard groups that aren't "
        "already in the database, you can add a comma-separated list "
        "here.")
        
    add_new_contributors = forms.CharField(max_length=100, required=False,
        help_text="If the people contributing to your project aren't "
        "already in the database, you can add a comma-separated list "
        "here.")
        
    class Meta:
        model = Project
        widgets = autocomplete_light.get_widgets_dict(Project)
        fields = ('name', 'short_description', 'description', 'url', 
                  'contact_email', 'contact_phone', 'units', 'add_new_groups',
                  'contributors', 'add_new_contributors', 'status', 
                  'start_date', 'end_date', 'elements', 'add_new_elements', 
                  'project_type')
