from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = patterns('',
    url(r'^$',
        views.ProjectListView.as_view(),
        name='list_view'),
    url(r'^(?P<pk>\d+)/$',
        views.ProjectDetailView.as_view(),
        name='detail_view'),
    url(r'^(?P<pk>\d+)/edit/$',
        login_required(views.ProjectEditView.as_view()),
        name='edit_view'),
    url(r'^new/$',
        login_required(views.ProjectCreateView.as_view()),
        name='create_view'),
    url(r'^random/$',
        views.ProjectRandomView.as_view(),
        name='random'),
    url(r'createelement',
        views.CreateElement,
        name='createelement'),
    url(r'createunit',
        views.CreateUnit,
        name='createunit'),
    url(r'createcontributor',
        views.CreateContributor,
        name='createcontributor'),
)
