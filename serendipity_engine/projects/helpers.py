"""
Abstracts out processing of new elements, groups, and contributors
not covered by the autocomplete in project creation. Code reuse FTW.
"""
from django.db.models.loading import get_model

def process_new_items(new_items, app_label, model_name):
    """
    Creates new database objects, if needed, for each comma-separated
    item in our new_items list
    """
    my_model = get_model(app_label, model_name)

    new_items = new_items.split(',')
    return_list = []
    for new_item in new_items:
        # only process if nonempty. Oddly, empty unicode strings
        # seem truthy.
        if new_item and not new_item==u'':
            # begone, spurious whitespace
            new_item = new_item.lstrip().rstrip()
            print new_item
            print new_item.isspace()
            try:
                # if they've somehow put something that's already in our
                # db into the new elements field, use the existing element
                item = my_model.objects.get(name__iexact=new_item)
            except my_model.DoesNotExist:
                # otherwise, create a new element
                item = my_model()
                item.name = new_item
                item.save()
            return_list += [item]
    return return_list

def process_new_item_fields(form, my_project):
    """
    Creates new database objects for elements, units, and contributors
    from the project creation form. Add them to the project's relationships.
    """
    new_elements = form.cleaned_data['add_new_elements']
    new_elements = process_new_items(new_elements, 'elements', 'Element')
    my_project.elements.add(*new_elements)

    new_units = form.cleaned_data['add_new_groups']
    new_units = process_new_items(new_units, 'units', 'Unit')
    my_project.units.add(*new_units)

    new_contributors = form.cleaned_data['add_new_contributors']
    new_contributors = process_new_items(new_contributors,
                          'units', 'Contributor')
    my_project.contributors.add(*new_contributors)

    my_project.save()
