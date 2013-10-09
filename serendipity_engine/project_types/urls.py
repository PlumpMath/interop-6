from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = patterns('',
    # Examples:
    url(r'^(?P<name>\w+)/$', 
        views.ProjectTypeDetailView.as_view(),
        name='detail_view'),
    url(r'^(?P<name>\d+)/edit/$', 
        login_required(views.ProjectTypeEditView.as_view()),
        name='edit_view'),
    url(r'^new/$', 
        login_required(views.ProjectTypeCreateView.as_view()),
        name='create_view'),
)