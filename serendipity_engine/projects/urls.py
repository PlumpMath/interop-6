from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = patterns('',
    # Examples:
    url(r'^(?P<pk>\d+)/$', 
        views.ProjectDetailView.as_view(),
        name='detail_view'),
    url(r'^(?P<pk>\d+)/edit/$', 
        login_required(views.ProjectEditView.as_view()),
        name='edit_view'),
    url(r'^new/$', 
        login_required(views.ProjectCreateView.as_view()),
        name='create_view'),
)
