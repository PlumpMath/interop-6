from django.views.generic import DetailView

from .models import Element

class ElementDetailView(DetailView):
    """
    Shows projects using this element.
    """
    model = Element
    template_name = "facet_detail.html"
