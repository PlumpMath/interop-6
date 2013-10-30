from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView

import autocomplete_light

# must go before admin.autodiscover()
autocomplete_light.autodiscover()

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from .views import HomeView, MiscellaneousView

urlpatterns = patterns('',
    url(r'^$',
        HomeView.as_view(),
        name='home'),
    url(r'^miscellaneous/$',
        MiscellaneousView.as_view(),
        name='miscellaneous'),
    url(r'^about/$',
        TemplateView.as_view(template_name='about.html'),
        name='about'),

    # app namespaces
    url(r'^projects/',
        include('serendipity_engine.projects.urls', namespace='projects')),
    url(r'^elements/',
        include('serendipity_engine.elements.urls', namespace='elements')),
    url(r'^types/',
        include('serendipity_engine.project_types.urls',
            namespace='project_types')),
    url(r'^groups/',
        include('serendipity_engine.units.urls', namespace='units')),

    # userauth URLs
    url(r'^accounts/login/$',
        'django.contrib.auth.views.login',
        name="login"),
    url(r'^accounts/logout/$',
        'django.contrib.auth.views.logout_then_login',
        name='logout'),
    url(r'^accounts/', include('registration.backends.default.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^autocomplete/', include('autocomplete_light.urls')),
)
