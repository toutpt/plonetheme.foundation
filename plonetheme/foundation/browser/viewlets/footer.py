
from plone.app.layout.viewlets import common
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class FooterViewlet(common.FooterViewlet,
                    common.SiteActionsViewlet):
    """Footer reviewed to include colophon and site actions"""
    index = ViewPageTemplateFile("footer.pt")

    def update(self):
        common.FooterViewlet.update(self)
        common.SiteActionsViewlet.update(self)
