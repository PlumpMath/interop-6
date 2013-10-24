import autocomplete_light

from serendipity_engine.elements.models import Element
from serendipity_engine.projects.models import Project
from serendipity_engine.units.models import Contributor, Unit

class NameAutocomplete(autocomplete_light.AutocompleteModelBase):
    search_fields = ['name']
autocomplete_light.register(Element, NameAutocomplete)
autocomplete_light.register(Project, NameAutocomplete)
autocomplete_light.register(Contributor, NameAutocomplete)
autocomplete_light.register(Unit, NameAutocomplete)
