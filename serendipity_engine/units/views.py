from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import DetailView, UpdateView

from serendipity_engine.projects.models import Project

from .forms import UnitUpdateForm, SchoolUpdateForm
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
        
    def get_context_data(self, **kwargs):
        context = super(UnitDetailView, self).get_context_data(**kwargs)
        context['edit_url'] = \
            reverse_lazy('units:unit_update_view', args=(self.object.id,))
        return context
        
class UnitUpdateView(UpdateView):
    model = Unit
    form_class = UnitUpdateForm

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS,
                             'Hooray, %s edited!'
                             % self.object.name)
        return reverse_lazy('units:detail_view', args=(self.object.id,))

class ContributorDetailView(DetailView):
    model = Contributor
    template_name = "contributor_detail.html"
    
    def get_context_data(self, **kwargs):
        context = super(ContributorDetailView, self).get_context_data(**kwargs)
        context['edit_url'] = \
            reverse_lazy('units:contributor_update_view', args=(self.object.id,))
        contributor_projects = \
            Project.objects.filter(contributors__id=self.object.id)
        contributor_units = \
            Unit.objects.filter(projects__in=contributor_projects)
        context['units'] = contributor_units
        if contributor_units:
            context['schools'] = \
                School.objects.filter(subunits__in=contributor_units)
        return context
        
class ContributorUpdateView(UpdateView):
    model = Contributor
    template_name = "units/unit_form.html"

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS,
                             'Hooray, %s edited!'
                             % self.object.name)
        return reverse_lazy('units:contributor_view', args=(self.object.id,))

class SchoolDetailView(DetailView):
    model = School
    template_name = "facet_detail.html"
    
    def get_context_data(self, **kwargs):
        context = super(SchoolDetailView, self).get_context_data(**kwargs)
        subunits = self.object.subunits.all()
        context['projects_override'] = \
            Project.objects.filter(units__in = subunits).order_by('?')
        context['edit_url'] = \
            reverse_lazy('units:school_update_view', args=(self.object.id,))
        return context

class SchoolUpdateView(UpdateView):
    model = School
    template_name = "units/unit_form.html"
    form_class = SchoolUpdateForm
    
    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS,
                             'Hooray, %s edited!'
                             % self.object.name)
        return reverse_lazy('units:school_view', args=(self.object.id,))