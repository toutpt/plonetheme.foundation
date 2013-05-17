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
        portal_skins = getToolByName(self.context, "portal_skins")
        portal_url = getToolByName(self.context, 'portal_url')()

        themename = portal_skins.getDefaultSkin()
        theme = themename + "desk"
        themes = portal_skins.getSkinSelections()
        if theme not in themes:
            theme = "plonetheme.foundationdesk"

        js = jstool.getCookedResources(theme=theme)
        js_info = []
        for script in js:
            url = '%s/portal_javascripts/%s/%s' % (
                portal_url,
                theme,
                script.getId(),
            )
            js_info.append(url)
        css = csstool.getCookedResources(theme=theme)
        css_info = []
        for sheet in css:
            url = '%s/portal_css/%s/%s' % (
                portal_url,
                theme,
                script.getId(),
            )
            css_info.append(url)

        resources = {"js": js_info, "css": css_info}
        json_resources = json.dumps(resources)
        self.request.response.setHeader("Content-type", "application/json")
        return json_resources
