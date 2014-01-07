from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
    # Examples:
    url(r'^(?P<pk>\w+)/$', 
        views.ProjectTypeDetailView.as_view(),
        name='detail_view'),
)