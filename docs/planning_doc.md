# Working document for the Serendipity Engine

## Pages list
* top page
* /project/X -- every project has a detail view
* /project/X/using -- list view of anything that uses this project
    maybe? this might just be in the detail view. Which would be metadata,
    using, uses, rest of stack.  With the share icons. Hooray sharing.
* /project/X/edit -- every project has an edit view (restricted to...?)
* /project/new
* /type/word -- every project type has a listview of projects
* /type/word/edit
* /type/new
* /element/word -- every non-interop ingredient has a listview of projects
* /element/word/edit
* /element/word/new
* /miscellaneous -- returns everything (with an <h1>Everything.</h1>)
* /unit/name -- every unit has a listview of projects
* /unit/name/edit
* /unit/name/new
* /school/name -- every school (or whatever the superset of unit is) has a listview of projects
* are schools editable/creatable?
    this will only work if I have a good way of associating those
* /login, /register
* /admin (moved appropriately)
* /random

Basic page types are listview and edit/create view (different views logic,
same template skeletons)

I can do show-hide in browser if everything has a class name driven by its database
ID. Clicking on a sidebar triggers show/hide of everything with the associated class.
Use highlighting and some other trigger to show active-ness.
This suggests an obvious responsive thing -- clickthrough or stay in place

There's a relationship of projects to *projects*. Someone may make a collection that
someone else uses.  Need to represent "things using this project".

More generally: need to see things that ARE ontologies (WLOG), and things that USE 
them.
"Show projects that are..."
"Show projects that use..."

Think about a share-icon kind of thing for "Interop projects using this..." 
"Interop projects this uses..." (just Share, really, maybe. flipped backward 
in one case.)
This IS the interop, right here.
And then there's a section of non-interop elements it uses. (with the list-ul icon
from FontAwesome, perhaps.)

Projects can use other Harvard projects, and they can also use external elements.
If users are allowed to enter interop projects they use, we may end up with
blank pages -- will need a "nothing here. add something?" kind of option.

## Facets

Type
Component (alpha)
Organization (ask DW about sub/superunits)

Keyword search??

### db schema for Facet:
foreignkey(FacetExample)
description

### db schema for FacetExample:
manytomany(projects)
description

So "Collection" is a facet, and specific collections are FacetExamples.
