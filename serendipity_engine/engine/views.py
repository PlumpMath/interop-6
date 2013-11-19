from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.sites.models import Site, RequestSite
from django.core.mail import send_mail
from django.core.urlresolvers import reverse_lazy, reverse
from django.db.models.signals import pre_save
from django.views.generic.base import TemplateView

from registration.forms import RegistrationFormUniqueEmail
from registration.models import RegistrationProfile
from registration.views import RegistrationView

from serendipity_engine.projects.models import Project

class HomeView(TemplateView):
    """
    The top level of the site.
    """
    template_name = "home.html"
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        # order_by('?') randomizes order of projects
        context['projects'] = Project.objects.all().order_by('?')
        return context

class MiscellaneousView(HomeView):
    """
    An Easter egg.
    """
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(MiscellaneousView, self).get_context_data(**kwargs)
        context['miscellaenous'] = True
        return context

class SerendipityRegistrationView(RegistrationView):
    """
    Overrides default django-registration to allow for manual
    activation of accounts.
    """
    form_class = RegistrationFormUniqueEmail
    success_url = reverse_lazy('registration_complete')

    def register(self, request, **cleaned_data):
        username, email, password = cleaned_data['username'], cleaned_data['email'], cleaned_data['password1']
        if Site._meta.installed:
            site = Site.objects.get_current()
        else:
            site = RequestSite(request)
        new_user = RegistrationProfile.objects.create_inactive_user(username, email,
                                                                    password, site)

        domain = Site.objects.get_current().domain
        send_mail('New interop user needs activation',
                  'An account for ' + username + ' with email address '
                  + email + ' has just been registered at the Harvard Interop '
                  'Serendipity Engine. If this is legit, please log into the '
                  'admin site (http://' + domain + reverse('admin:index') +
                  ') and activate the account.',
                  settings.FROM_EMAIL,
                  settings.INTEROP_ADMINS)
        return new_user


def activate_user(sender, **kwargs):
    try:
        instance = kwargs['instance']
        user = User.objects.get(username=instance.username)
        domain = Site.objects.get_current().domain
        if (user.is_active == False and instance.is_active == True):
            send_mail('Woot! Your Harvard Interop account is live.',
                      'Your Harvard interop account has been approved. '
                      'You can now log in at http://' + domain +
                      reverse('login') + ' with the username '
                      + instance.username + ' and the password you set when '
                      'you created your account.\n\n'
                      'Create a new project at http://' + domain + 
                      reverse('projects:create_view') + '.\n\n'
                      'Forgot your password? You can reset it at http://' +
                      domain +
                      reverse('django.contrib.auth.views.password_reset')
                      + ' .',
                      settings.FROM_EMAIL,
                      settings.INTEROP_ADMINS)

    except User.DoesNotExist:
        # if User.DoesNotExist, we're registering and haven't saved them to db
        # yet. No need to do anything; we only send activation emails on the
        # second step of our two-step registration
        pass
pre_save.connect(activate_user, sender=User)
