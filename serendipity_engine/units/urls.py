from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
    url(r'^(?P<pk>\d+)/$',
        views.UnitDetailView.as_view(),
        name='detail_view'),
    url(r'^(?P<pk>\d+)/edit/$',
        views.UnitUpdateView.as_view(),
        name='unit_update_view'),
    url(r'^people/(?P<pk>\d+)/$',
        views.ContributorDetailView.as_view(),
        name='contributor_view'),
    url(r'^people/(?P<pk>\d+)/edit/$',
        views.ContributorUpdateView.as_view(),
        name='contributor_update_view'),
    url(r'^schools/(?P<pk>\d+)/$',
        views.SchoolDetailView.as_view(),
        name='school_view'),
    url(r'^schools/(?P<pk>\d+)/edit/$',
        views.SchoolUpdateView.as_view(),
        name='school_update_view'),
)