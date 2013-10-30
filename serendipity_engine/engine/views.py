from django.views.generic.base import TemplateView
from serendipity_engine.projects.models import Project

class HomeView(TemplateView):
    template_name = "home.html"
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        # order_by('?') randomizes order of projects
        context['projects'] = Project.objects.all().order_by('?')
        return context
    
class MiscellaneousView(HomeView):
    """
    An Easter egg.
    """
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(MiscellaneousView, self).get_context_data(**kwargs)
        context['miscellaenous'] = True
        return context
