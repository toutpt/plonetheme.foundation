"""The origin plone-edit bar is a set of two menus:

IContentViews is a viewletmanager with:

* contentactions: plone.app.layout.viewlets.contentactions.pt
* contentviews: plone.app.layout.viewlets.contentviews.pt

contentviews
------------

* folderContents
* view
* edit
* contentrules
* local_roles

contentactions
--------------

* contentmenu-workflow (state)
* contentmenu-factories (add)
* contentmenu-display (display mode)

In plonetheme.foundation we switch to a one menu with all things in it

So original viewlets are hidden by the profile
"""

from plone.app.layout.viewlets.common import ContentActionsViewlet
from plone.app.layout.viewlets.common import ContentViewsViewlet
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class EditBar(ContentActionsViewlet, ContentViewsViewlet):
    """Edit bar as foundation menu"""
    index = ViewPageTemplateFile("editbar.pt")

    def update(self):
        ContentActionsViewlet.update(self)
        ContentViewsViewlet.update(self)
