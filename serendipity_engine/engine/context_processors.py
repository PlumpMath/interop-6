from elements.models import Element
from project_types.models import ProjectType
from units.models import Unit

def sidebar_context(request):
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