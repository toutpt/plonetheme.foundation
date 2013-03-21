import json
from plone.app.layout.viewlets.common import ViewletBase
from Products.Five.browser import BrowserView
from Products.CMFCore.utils import getToolByName


class ResourcesViewlet(ViewletBase):
    """This viewlet is responsible to load resources from the theme desktop"""

    def update(self):
        super(ResourcesViewlet, self).update()


class Resources(BrowserView):
    """Return data structure for enquire js script"""
    def __call__(self):
        jstool = getToolByName(self.context, "portal_javascripts")
        csstool = getToolByName(self.context, "portal_css")
        portal_url = getToolByName(self.context, 'portal_url')()
        js = jstool.getCookedResources(theme="plonetheme.foundationdesk")
        js_info = []
        for script in js:
            js_info.append(portal_url + '/' + script.getId())

        css = csstool.getCookedResources(theme="plonetheme.foundationdesk")
        css_info = []
        for sheet in css:
            css_info.append(portal_url + '/' + sheet.getId())

        resources = {"js": js_info, "css": css_info}
        json_resources = json.dumps(resources)
        self.request.response.setHeader("Content-type", "application/json")
        return json_resources
