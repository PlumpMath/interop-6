from django.views.generic import DetailView

from .models import Unit

class UnitDetailView(DetailView):
    model = Unit
    template_name = "facet_detail.html"