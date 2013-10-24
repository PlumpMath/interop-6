from django.views.generic.base import TemplateView, RedirectView
from serendipity_engine.projects.models import Project
  
class HomeView(TemplateView):
    template_name = "home.html"      
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['projects'] = Project.objects.all()
        return context
    
class MiscellaneousView(HomeView):
    template_name = "home.html"      

    def get_context_data(self, **kwargs):
        context = super(MiscellaneousView, self).get_context_data(**kwargs)
        context['miscellaenous'] = True
        return context