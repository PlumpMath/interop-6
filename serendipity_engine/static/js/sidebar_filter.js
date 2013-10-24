var $j = jQuery.noConflict();

$j(document).ready(function() {
    var showList = [];
    var harvest_identifier = function(element) {
        // we have to do id_facet and class_facet as id/class
        // names on elements rather than just id="facet",
        // class="facet" because facet names are not guaranteed
        // to be valid CSS selectors
        id = element.attr("id")
        id = id.slice(3);
        return id
    }
    
    // this shows or hides tiles based on the facets listed in the sidebar
    // of the home page, which are ORed together.
    var toggle_all_the_things = function(identifier) {
        // native JS indexOf doesn't work with IE. Use 
        // jQuery instead.
        if($j.inArray(identifier, showList) >= 0) {
            // if this facet was in our list of things to show,
            // remove it.
            showList.splice($j.inArray(identifier, showList), 1);
            
            // if there's nothing in the facet list any more, stop
            // filtering: show everything
            if(showList.length <= 0) {
                $j('.tile').each(function() {
                    $j(this).css('display','inherit');
                });
                return;
            }

            // process each project which has the facet the user clicked on in 
            // the sidebar. If we're supposed to show it because of some other 
            // facet it has, leave it alone. Otherwise hide it.
            $j('.class_' + identifier).each(function() {
                var element = $j(this);
                var hide_condition = 1;
                classlist = element.attr('class').split(' ');
                for (var index in classlist) {
                    // if any of the element's classes are in the list of 
                    // things we show, flip our test condition and exit the 
                    // for loop: no need to look further
                    facet = classlist[index].slice(6);
                    if($j.inArray(facet, showList) >= 0) {
                        hide_condition = 0;
                        return;
                    }
                }
                if(hide_condition==1){
                    element.css('display', 'none');
                }
            });
            
        } else {
            // if this class was NOT already in our list of things to show, 
            // add it, and reveal all elements of this type.
            if(showList.length <= 0) {
                // if we haven't been filtering anything yet,
                // start to: hide everything not selected
                $j('.tile').each(function() {
                    $j(this).css('display', 'none');
                });
            }
            showList.push(identifier);
            $j('.class_' + identifier).each(function() {
                if ($j(this).css('display')=='none') {
                    $j(this).css('display', 'inherit');
                }
            });
        }
    }
    
    $j('.facetlist li').click(function() {
        $j(this).toggleClass('active');
        identifier = harvest_identifier($j(this));
        toggle_all_the_things(identifier);
    });
});