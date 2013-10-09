from django.views.generic import (ListView,
                                  DetailView, 
                                  UpdateView,
                                  CreateView)
                                  
from .models import Project
                                  
class ProjectListView(ListView):
    model = Project
