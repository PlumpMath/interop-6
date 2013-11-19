from django import forms

import autocomplete_light
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Field, Fieldset, Submit

from .models import Project
from serendipity_engine.units.models import Unit

class ProjectForm(autocomplete_light.FixedModelForm):
    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['add_new_elements'].label = "Add new building blocks"
        self.fields['description'].label = "(Optional) long description"
        self.helper.layout = Layout(
            Fieldset(
                "Basic project information",
                Div(
                    Div(
                        'name',
                        'url', 
                        'short_description',
                        css_class='span6'
                    ),
                    Div(
                        'description',
                        css_class='span6'
                    ),
                    css_class="row-fluid"
                ),
            ),
            Fieldset(
                "Building blocks",
                'project_type',
                Div(
                    Div('elements',
                        css_class='span6'
                    ),
                    Div('add_new_elements',
                        css_class='span6'
                    ),
                    css_class="row-fluid"
                ),
            ),
            Fieldset(
                "People and contact information",
                'contact_email',
                'contact_phone',
                Div(
                    Div('units',
                        css_class='span6'
                    ),
                    Div('add_new_groups',
                        css_class='span6'
                    ),
                    css_class="row-fluid"
                ),
                Div(
                    Div('contributors',
                        css_class='span6'
                    ),
                    Div('add_new_contributors',
                        css_class='span6'
                    ),
                    css_class="row-fluid"
                ),
            ),
            Fieldset(
                "Status",
                Div(
                    Div(
                        Field(
                            'start_date',
                            css_class='datepicker'
                        ),
                        css_class='span6'
                    ),
                    Div(
                        Field(
                            'end_date',
                            css_class='datepicker'
                        ),
                        css_class='span6'
                    ),
                    css_class="row-fluid"
                ),
                'status', 
            ),
        )
        self.helper.add_input(Submit('submit', 'Submit'))
        
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
