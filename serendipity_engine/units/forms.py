from django import forms

from .models import Unit, School

class UnitUpdateForm(forms.ModelForm):
    # Makes it possible to associate units with schools through front end.
    school = forms.ModelChoiceField(queryset=School.objects.all().order_by('name'),
                                    empty_label="(No school)", 
                                    required=False)

    class Meta:
        model = Unit
        fields = ('name', 'url')
        
class SchoolUpdateForm(forms.ModelForm):
    # Overrides the default widget to allow for empty input.
    subunits = forms.ModelMultipleChoiceField(queryset=Unit.objects.all(),
                                              required=False)
    
    class Meta:
        model = School
        fields = ('subunits',)
