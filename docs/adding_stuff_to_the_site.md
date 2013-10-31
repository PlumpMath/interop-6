# Altering the site

## To change the sidebar...
* it lives in serendipity_engine/templates/sidebar.html
* linking to external sites is standard HTML: just add <li>
  <a href="your link">your linktext</a></li>
* for linking to internal pages you can use Django magic (the invocation
  won't change even if you someday change the URL structure):
  <li><a href="{% url 'namespace:name' %}">your linktext</a></li> for
  URLs that don't have parameters, or <li>
  <a href="{% url 'namespace:name' arg1 %}">your linktext</a>
  </li> for URLs that do have parameters.  See sidebar.html for examples.
  
## To add flat pages...
* Copy serendipity_engine/templates/flatpage.html to 
  serendipity_engine/templates/yournewpage.html
* Replace the lipsum. (Don't touch the Django syntax that surrounds it.)
  Go ahead and use your favorite HTMLs.  This will create a page like the
  About page.
* Add a URL for the page so that Django can find it:
    * in serendipity_engine/engine/urls.py...
    * add lines that look like...
    
      url(r'^yoururl/$',
        TemplateView.as_view(template_name='yournewpage.html'),
        name='yourpagename'),
      
* FUN FACT! You will now be able to reference this page in other Django
  templates with the invocation {% url 'yourpagename' %}.  Even if you
  change yoururl, as long as yourpagename stays the same, the invocation
  will find it.  Hooray!