from random import randint

from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import (ListView,
                                  DetailView, 
                                  UpdateView,
                                  CreateView)
                                  
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