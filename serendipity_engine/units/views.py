from django.views.generic import DetailView

from .models import Unit, Contributor

class UnitDetailView(DetailView):
    model = Unit
    template_name = "facet_detail.html"
    
class ContributorDetailView(DetailView):
    model = Contributor
    template_name = "facet_detail.html"