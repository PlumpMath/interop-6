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

        # override form field labels
        self.fields['description'].label = "(Optional) long description"
        self.fields['api'].label = "Does this project offer an API "\
            "or other programmatic access (data download, OAI-PMH, etc.)? " \
            "Check if yes."
        self.fields['api_doc_link'].label = "Link to documentation for API "\
            "or other programmatic access, if applicable"
        self.fields['projects_interoperated_with'].label = "Other Harvard " \
            "projects this uses, or is used by"
        self.fields['units'].help_text = "Group(s) with primary responsibility " \
            "for the project. To specify which Harvard school a group " \
            "belongs to, edit that group directly."
        # prevent the projects-interoperated-with select widget from
        # including the project itself as a choice of projects to link to
        self.fields['projects_interoperated_with'].queryset = \
            Project.objects.exclude(id=self.instance.id)

        # make the form pretty
        self.helper.layout = Layout(
            Fieldset(
                "Basic project information",
                Div(
                    Div(
                        'name',
                        'display_name',
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
                "Building blocks and interoperability hooks",
                'project_type',
                Div(
                    Div('elements',
                        css_class='span6'
                    ),
                    css_class="row-fluid"
                ),
                'projects_interoperated_with',
                'api',
                'api_doc_link',
            ),
            Fieldset(
                "People and contact information",
                'contact_email',
                'contact_phone',
                Div(
                    Div('units',
                        css_class='span6'
                    ),
                    css_class="row-fluid"
                ),
                Div(
                    Div('contributors',
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

    class Meta:
        model = Project
        widgets = autocomplete_light.get_widgets_dict(Project)
        fields = ('name', 'short_description', 'description', 'url',
                  'contact_email', 'contact_phone', 'units',
                  'contributors', 'status',
                  'start_date', 'end_date', 'elements',
                  'project_type', 'api', 'api_doc_link', 'display_name',
                  'projects_interoperated_with')
