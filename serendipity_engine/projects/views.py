from random import randint
import json

from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import (ListView,
                                  DetailView,
                                  UpdateView,
                                  CreateView)

from serendipity_engine.elements.models import Element

from .forms import ProjectForm
from .helpers import process_new_item_fields, process_new_items
from .models import Project

def CreateElement(request):
    element = request.POST.get('element','')
    new_element = []
    if element:
        new_element = process_new_items(element, 'elements', 'Element')
    if new_element:
        rval = new_element
    else:
        # Already exists
        return HttpResponse('',status=422,content_type='text/json')

    return HttpResponse(json.dumps(rval),status=201,content_type='text/json')

def CreateUnit(request):
    group = request.POST.get('unit','')
    new_group = []
    if group:
        new_group = process_new_items(group, 'units', 'Unit')
    if new_group:
        rval = new_group
    else:
        # Already exists
        return HttpResponse('',status=422,content_type='text/json')

    return HttpResponse(json.dumps(rval),status=201,content_type='text/json')

def CreateContributor(request):
    contributor = request.POST.get('contributor','')
    new_contributor = []
    if contributor:
        new_contributor = process_new_items(contributor, 'units', 'Contributor')
    if new_contributor:
        rval = new_contributor
    else:
        # Already exists
        return HttpResponse('',status=422,content_type='text/json')

    return HttpResponse(json.dumps(rval),status=201,content_type='text/json')


class ProjectListView(ListView):
    model = Project

class ProjectDetailView(DetailView):
    model = Project

class ProjectEditView(UpdateView):
    model = Project
    form_class = ProjectForm

    def form_valid(self, form):
        super(ProjectEditView, self).form_valid(form)
        #process_new_item_fields(form, self.object)
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        print 'get url'
        stored_messages = messages.get_messages(self.request)
        if not stored_messages:
            """
            get_success_url gets called twice by form_valid (once
            by the super call, once by the ending redirect). Want to
            make sure we only add the success message once.
            """
            messages.add_message(self.request, messages.SUCCESS,
                                 'Hooray, project edited!')
        print "ksdlkfhdsjkfhskdfhskdjfhksjfhdjksf"
        return reverse_lazy('projects:detail_view', args=(self.object.id,))

class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectForm

    def get_context_data(self, **kwargs):
        context = super(ProjectCreateView, self).get_context_data(**kwargs)
        context['datepicker_needed'] = True
        return context

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR,
            "Whoops, that project couldn't be created as specified. Please fix "
            "the errors below.")
        return super(ProjectCreateView, self).form_invalid(form)

    def form_valid(self, form):
        # object needs to exist before we can add manytomany relationships
        super(ProjectCreateView, self).form_valid(form)
        self.object = form.save()
        process_new_item_fields(form, self.object)
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        stored_messages = messages.get_messages(self.request)
        if not stored_messages:
            """
            get_success_url gets called twice by form_valid (once
            by the super call, once by the ending redirect). Want to
            make sure we only add the success message once.
            """
            messages.add_message(self.request, messages.SUCCESS,
                                 'Hooray, %s created!'
                                 % self.object.name)
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
