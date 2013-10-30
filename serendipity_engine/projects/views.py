from random import randint

from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import (ListView,
                                  DetailView, 
                                  UpdateView,
                                  CreateView)

from serendipity_engine.elements.models import Element

from .models import Project
from .forms import ProjectForm
                                  
class ProjectListView(ListView):
    model = Project

class ProjectDetailView(DetailView):
    model = Project

class ProjectEditView(UpdateView):
    model = Project
    form_class = ProjectForm

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS,
                             'Hooray, project edited!')
        return reverse_lazy('projects:detail_view', args=(self.object.id,))

class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectForm
    
    def form_valid(self, form):
        # object needs to exist before we can add manytomany relationships
        self.object = form.save()
        new_elements = form.cleaned_data['add_new_elements']
        new_elements = new_elements.split(',')
        
        for new_element in new_elements:
            # begone, spurious whitespace
            new_element = new_element.lstrip().rstrip()
            try:
                # if they've somehow put something that's already in our
                # db into the new elements field, use the existing element
                element = Element.objects.get(name__iexact=new_element)
            except:
                # otherwise, create a new element
                element = Element()
                element.name = new_element
                element.save()
            self.object.elements.add(element)
        return super(ProjectCreateView, self).form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('projects:detail_view', args=(self.object.id,))
        
class ProjectRandomView(DetailView):
    model = Project
    
    def dispatch(self, request, *args, **kwargs):
        if Project.objects.count() == 0:
            # the randint in get_object is only well-defined if there are projects
            return HttpResponseRedirect('/')
        else:
            return super(ProjectRandomView, self).dispatch(request, *args, **kwargs)
    
    def get_object(self):
        count = Project.objects.count()
        random_index = randint(0, count - 1)
        return Project.objects.all()[random_index]