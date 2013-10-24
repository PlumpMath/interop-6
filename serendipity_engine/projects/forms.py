from django import forms

import autocomplete_light

from .models import Project
from serendipity_engine.units.models import Unit

class ProjectForm(autocomplete_light.FixedModelForm):
    class Meta:
        model = Project
        widgets = autocomplete_light.get_widgets_dict(Project)
        fields = ('name', 'description', 'url', 'contact_email',
                  'contact_phone', 'office_location', 'units', 
                  'contributors', 'status', 'start_date', 'end_date',
                  'elements', 'project_type')
