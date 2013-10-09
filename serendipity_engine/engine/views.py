from django.views.generic.base import TemplateView, RedirectView
  
class HomeView(TemplateView):
    template_name = "home.html"      
    
class MiscellaneousView(TemplateView):
    template_name = "home.html"      

    def get_context_data(self, **kwargs):
        context = super(MiscellaneousView, self).get_context_data(**kwargs)
        context['miscellaenous'] = True
        return context
        
class RandomView(RedirectView):
    pass