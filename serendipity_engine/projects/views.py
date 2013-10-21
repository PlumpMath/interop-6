from random import randint

from django.core.urlresolvers import reverse_lazy
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

class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectForm
    
    def get_success_url(self):
        return reverse_lazy('projects:detail_view', args=(self.object.id,))
        
class ProjectRandomView(DetailView):
    model = Project
    
    def get_object(self):
        count = Project.objects.count()
        random_index = randint(0, count - 1)
        return Project.objects.all()[random_index]