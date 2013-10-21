from django.views.generic import DetailView

from .models import ProjectType

class ProjectTypeDetailView(DetailView):
    model = ProjectType        
    template_name = "facet_detail.html"