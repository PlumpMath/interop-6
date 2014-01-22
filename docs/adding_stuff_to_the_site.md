# Altering the site

## To approve users...
* Log in to the admin site at /admin .
* Click on Users
* Click on the user you would like to approve
* Click on the Active checkbox
* Save the user

Newly activated users will automatically get an email telling them how
to add a project and reminding them of their username.

## To change the sidebar...
* it lives in serendipity_engine/templates/sidebar.html
* linking to external sites is standard HTML: just add `<li>
  <a href="your link">your linktext</a></li>`
* for linking to internal pages you can use Django magic (the invocation
  won't change even if you someday change the URL structure):
  `<li><a href="{% url 'namespace:name' %}">your linktext</a></li>` for
  URLs that don't have parameters, or `<li>
  <a href="{% url 'namespace:name' arg1 %}">your linktext</a>
  </li>` for URLs that do have parameters.  See sidebar.html for examples.
  
## To add flat pages...
* Copy serendipity_engine/templates/flatpage.html to 
  serendipity_engine/templates/yournewpage.html
* Replace the lipsum. (Don't touch the Django syntax that surrounds it.)
  Go ahead and use your favorite HTMLs.  This will create a page like the
  About page.
* Add a URL for the page so that Django can find it:
    * in serendipity_engine/engine/urls.py...
    * add lines that look like...
    
      `url(r'^yoururl/$',
        TemplateView.as_view(template_name='yournewpage.html'),
        name='yourpagename'),`
      
* FUN FACT! You will now be able to reference this page in other Django
  templates with the invocation `{% url 'yourpagename' %}`.  Even if you
  change yoururl, as long as yourpagename stays the same, the invocation
  will find it.  Hooray!

### Example
* Let's say you've created a file serendipity_engine/templates/cluetrain.html , and replaced the lipsum with your preferred content.
* In serendipity_engine/engine/urls.py , you need to add some lines to give this file a URL.  You can do that anywhere before the closing parenthesis, but it's best to keep it together with the other flat page URLs, so the file will stay organized for future readers. So the section of the file that looks like:
```
    url(r'^about/$',
        TemplateView.as_view(template_name='about.html'),
        name='about'),

    # app namespaces
```
will now look like...
```
    url(r'^about/$',
        TemplateView.as_view(template_name='about.html'),
        name='about'),
    url(r'^cluetrain/$',
        TemplateView.as_view(template_name='cluetrain.html'),
        name='cluetrain'),

    # app namespaces
```
(You can make the URL and the name anything you want.  template_name needs to be the name of the file.  You don't need the path to the file, as long as it's in a template/ directory - Django will find it.)

* You can now refer to the page in Django templates with the name you just defined.  (This is awesome, as it means you can change the URLs things live at and never have to change the references in your templates.)  To do so, format links thusly:
```
<a href="{% url 'cluetrain' %}">my new cluetrain page</a>
```
