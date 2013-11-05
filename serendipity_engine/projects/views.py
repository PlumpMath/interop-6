from random import randint

from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import (ListView,
                                  DetailView,
                                  UpdateView,
                                  CreateView)

from serendipity_engine.elements.models import Element

from .forms import ProjectForm
from .helpers import process_new_item_fields
from .models import Project

class ProjectListView(ListView):
    model = Project

class ProjectDetailView(DetailView):
    model = Project

class ProjectEditView(UpdateView):
    model = Project
    form_class = ProjectForm

    def form_valid(self, form):
        process_new_item_fields(form, self.object)
        return HttpResponseRedirect(self.get_success_url())

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
        process_new_item_fields(form, self.object)
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS,
                             'Hooray, project created!')
        return reverse_lazy('projects:detail_view', args=(self.object.id,))

class ProjectRandomView(DetailView):
    model = Project

    def dispatch(self, request, *args, **kwargs):
        if Project.objects.count() == 0:
            # the randint in get_object is only well-defined if there are
            # projects
            return HttpResponseRedirect('/')
        else:
            return super(ProjectRandomView, self).dispatch(request,
                                                          *args,
                                                          **kwargs)

    def get_object(self):
        count = Project.objects.count()
        random_index = randint(0, count - 1)
        return Project.objects.all()[random_index]
