from django.db.models.loading import get_model

def process_new_items(new_items, app_label, model_name):
    my_model = get_model(app_label, model_name)
    
    new_items = new_items.split(',')
    return_list = []
    for new_item in new_items:
        if not new_item.isspace():
          # begone, spurious whitespace
          new_item = new_item.lstrip().rstrip()
          try:
              # if they've somehow put something that's already in our
              # db into the new elements field, use the existing element
              item = my_model.objects.get(name__iexact=new_item)
          except:
              # otherwise, create a new element
              item = my_model()
              item.name = new_item
              item.save()
          return_list += [item]
    return return_list
    
def process_new_item_fields(form, object):
    new_elements = form.cleaned_data['add_new_elements']
    new_elements = process_new_items(new_elements, 'elements', 'Element')
    object.elements.add(*new_elements)
    
    new_units = form.cleaned_data['add_new_groups']
    new_units = process_new_items(new_units, 'units', 'Unit')
    object.units.add(*new_units)

    new_contributors = form.cleaned_data['add_new_contributors']
    new_contributors = process_new_items(new_contributors, 
                          'units', 'Contributor')
    object.contributors.add(*new_contributors)
    
    object.save()
