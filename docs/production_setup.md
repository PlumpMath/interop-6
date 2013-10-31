# Yaks you'll need to shave in production

## In the environment
* Set up a virtualenv and install requirements.txt to it.
* Set a DJANGO_SETTINGS_MODULE environment variable to point at the
  production settings file 
  (`export DJANGO_SETTINGS_MODULE=serendipity_engine.engine.settings.production`)
* Set up a mysql db for the project.
* Make sure email sending functionality exists
* set a DJANGO_EMAIL_PASSWORD environment variable with the pw your
  user will need to log into your email sending functionality (no
  passwords in Django settings files themselves!)

## In serendipity_engine/engine/settings/production.py
* Edit DATABASES in production.py to point to your MySQL db.
* Edit ALLOWED_HOSTS in production.py to contain string(s) of the URL(s)
  you'll be serving the project from.
* You may want to customize your logging configuration (LOGGING in
  production.py); the default does not log very much.
* Configure email-sending variables
* add one or more ADMINS whom the app can email upon critical errors
* Configure FROM_EMAIL (the apparent sender of emails from the app)
* Configure INTEROP_ADMINS (to whom will the site send mail when it needs
  someone to activate an account; presumably David Weinberger)

## In the Django admin (/admin)
* change the URL on the default Site object to the base domain
  the project will live at.
* add project types ("Collections", "Ontologies, Schemas, APIs",
  etc.)
* Don't touch Auth:Groups, Registration:Registration profiles, or Sites:Site 
  (after you have changed the URL on the default object) unless you know
  what you're doing.
  
## Other Django stuff
* When you first turn it on, you'll need to `python manage syncdb --migrate`.
  This will establish the database schema.  It will also ask you if you want
  to create a superuser.  Say yes.
* If that superuser isn't David Weinberger, create him (in /admin is simplest) 
  as an active staff or superuser.
* Once you've configured him, test-register an account through
  /accounts/register. INTEROP_ADMINS should get a notification email. The user 
  should get a confirmation email upon registering the account, and a
  welcome email once David activates the account.
