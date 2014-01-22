from serendipity_engine.elements.models import Element
from serendipity_engine.project_types.models import ProjectType
from serendipity_engine.units.models import Unit

def sidebar_context(request):
    """
    Needed to render the lists in the navigation sidebar.
    """
    elements = Element.objects.all()
    project_types = ProjectType.objects.all()
    units = Unit.objects.all()

    return {'elements':elements,
            'project_types': project_types,
            'units': units}

def show_sidebar_url(request):
    if request.path == '/':
        url = False
    else:
        url = True
    return {'show_sidebar_url':url}
