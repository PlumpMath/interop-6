from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import DetailView

from serendipity_engine.projects.models import Project

from .models import Unit, Contributor, School

class UnitDetailView(DetailView):
    model = Unit
    template_name = "facet_detail.html"
    
    def dispatch(self, request, *args, **kwargs):
        print self.get_object()
        if self.get_object() in School.objects.all():
            url = reverse_lazy('units:school_view', args=(self.id,))
            return HttpResponseRedirect(url)
        return super(UnitDetailView, self).dispatch(request, *args, **kwargs)
    
class ContributorDetailView(DetailView):
    model = Contributor
    template_name = "facet_detail.html"
    
class SchoolDetailView(DetailView):
    model = School
    template_name = "facet_detail.html"
    
    def get_context_data(self, **kwargs):
        context = super(SchoolDetailView, self).get_context_data(**kwargs)
        context['projects_override'] = Project.objects.filter(units__in = self.object.subunits.all())
        return context
