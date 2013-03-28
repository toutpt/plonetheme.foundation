from zope import interface
from zope.i18n import translate
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.statusmessages.interfaces import IStatusMessage

from Products.CMFPlone import PloneMessageFactory as _p
from plone.app.layout.dashboard.dashboard import DashboardView
from plone.app.portlets.browser import manage
from plonetheme.foundation.browser import common


class IFoundationDashboard(interface.Interface):
    """marker interface"""


class FoundationDashboard(common.DisableBorderView, DashboardView):
    interface.implements(IFoundationDashboard)

    index = ViewPageTemplateFile('dashboard.pt')

    def __call__(self):
        self.update()
        return self.index()

    def update(self):
        super(FoundationDashboard, self).update()
        if self.empty() and self.can_edit():
            status = IStatusMessage(self.request)
            msg = _p(u"info_empty_dashboard")
            msg = translate(msg, domain='plone', context=self.request)
            status.add(msg, "info")


class ManageDashboardPortlets(manage.ManageDashboardPortlets,
                              common.DisableBorderView):
    interface.implements(IFoundationDashboard)

    def __call__(self):
        self.update()
        return self.index()
