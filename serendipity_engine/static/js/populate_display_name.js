$(document).ready(function() {
    var full_name = $('#id_name');
    var display_name = $('#id_display_name');
    // If the full name field has something in it on focusout and the
    // display name field is blank, populate display name with full name.
    // Display name is limited to 35 characters so this will throw a 
    // validation error if the full name is long, but best to let the
    // user decide how to abbreviate rather than to arbitrarily truncate.
    full_name.change(function() {
        if(full_name.val()!='' && display_name.val()=='') {
            display_name.val(full_name.val());
        }
    });
});