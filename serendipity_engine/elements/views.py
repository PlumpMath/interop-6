from django.views.generic import DetailView

from .models import Element

class ElementDetailView(DetailView):
    model = Element
    template_name = "facet_detail.html"