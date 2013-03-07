"""We override the sections viewlet of plone to add search box and
personal tools. No change to original code"""

from plone.app.layout.viewlets import common
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class GlobalSectionsViewlet(
    common.GlobalSectionsViewlet,
    common.SearchBoxViewlet,
    common.PersonalBarViewlet):
    """A super section bar"""
    index = ViewPageTemplateFile("sections.pt")

    def update(self):
        common.GlobalSectionsViewlet.update(self)
        common.SearchBoxViewlet.update(self)
        common.PersonalBarViewlet.update(self)
