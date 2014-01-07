from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
    url(r'^(?P<pk>\d+)/$',
        views.ElementDetailView.as_view(),
        name='detail_view'),
)
