"""We override the sections viewlet of plone to add search box and
personal tools. No change to original code"""

from plone.app.layout.viewlets import common
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.viewlet.interfaces import IViewletManager
from plone.app.viewletmanager.manager import OrderedViewletManager,\
    BaseOrderedViewletManager
from zope.component._api import getMultiAdapter

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


class ITopBarManager(IViewletManager):
    """A viewlet manager that sits in the <head> of the rendered page
    """


class ITopBarLeftManager(IViewletManager):
    """A viewlet manager that sits in the <head> of the rendered page
    """


class ITopBarRightManager(IViewletManager):
    """A viewlet manager that sits in the <head> of the rendered page
    """


class TopBarManager(BaseOrderedViewletManager):
    """manager"""
    template = ViewPageTemplateFile("topbar.pt")

    @property
    def portal_state(self):
        return getMultiAdapter((self.context, self.request),
                               name=u'plone_portal_state')

    def site_url(self):
        return self.portal_state.portal_url()

    def portal_title(self):
        return self.portal_state.portal_title()


class TopBarLeftManager(OrderedViewletManager):
    """manager"""
    template = ViewPageTemplateFile("topbar-left.pt")
    manager_template = ViewPageTemplateFile('topbar-manage-viewletmanager.pt')


class TopBarRightManager(OrderedViewletManager):
    """manager"""
    template = ViewPageTemplateFile("topbar-right.pt")
    manager_template = ViewPageTemplateFile('topbar-manage-viewletmanager.pt')


class EditBarViewlet(common.ContentActionsViewlet, common.ContentViewsViewlet):
    """A super edit bar"""

    def update(self):
        common.ContentActionsViewlet.update(self)
        common.ContentViewsViewlet.update(self)
