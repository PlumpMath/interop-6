from django import forms

import autocomplete_light

from .models import Project
from serendipity_engine.units.models import Unit

class ProjectForm(autocomplete_light.FixedModelForm):
    class Meta:
        model = Project
        widgets = autocomplete_light.get_widgets_dict(Project)

        print widgets