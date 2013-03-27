from plone.app.layout.dashboard.dashboard import DashboardView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.statusmessages.interfaces import IStatusMessage
from Products.CMFPlone import PloneMessageFactory as _p


class FoundationDashboard(DashboardView):

    index = ViewPageTemplateFile('dashboard.pt')

    def __call__(self):
        self.update()
        return self.index()

    def update(self):
        self.request.set('disable_border', 1)
        self.request.set('disable_plone.leftcolumn', 1)
        self.request.set('disable_plone.rightcolumn', 1)
        if self.empty() and self.can_edit():
            status = IStatusMessage(self.request)
            msg = self.context.translate(_p(u"info_empty_dashboard"))
            status.add(msg, "info")
