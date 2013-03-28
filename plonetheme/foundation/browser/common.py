from Products.Five.browser import BrowserView


class DisableBorderView(BrowserView):
    """Disable border of the view"""

    def update(self):
        self.request.set('disable_border', 1)
        self.request.set('disable_plone.leftcolumn', 1)
        self.request.set('disable_plone.rightcolumn', 1)
