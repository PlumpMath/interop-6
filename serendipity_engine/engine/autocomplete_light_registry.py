import autocomplete_light

from elements.models import Element
from projects.models import Project
from project_types.models import ProjectType
from units.models import Contributor, Unit

class NameAutocomplete(autocomplete_light.AutocompleteModelBase):
    search_fields = ['name']
autocomplete_light.register(Element, NameAutocomplete)
autocomplete_light.register(Project, NameAutocomplete)
autocomplete_light.register(Contributor, NameAutocomplete)
autocomplete_light.register(Unit, NameAutocomplete)
