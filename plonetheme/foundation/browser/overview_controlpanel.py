from plone.app.controlpanel import overview
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class OverviewControlPanel(overview.OverviewControlPanel):
    template = ViewPageTemplateFile("overview-controlpanel.pt")
