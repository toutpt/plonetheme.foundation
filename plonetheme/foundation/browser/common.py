from zope import component
from Products.Five.browser import BrowserView
from Products.CMFCore.utils import getToolByName


class BaseView(BrowserView):
    def __init__(self, context, request):
        self.context = context
        self.request = request
        self.cached_tools = {}
        self.cached_components = {}

    def __call__(self):
        self.update()
        return self.index()

    def update(self):
        pass

    def get_tool(self, toolname):
        if not toolname in self.cached_tools:
            self.cached_tools[toolname] = getToolByName(self.context, toolname)
        return self.cached_tools[toolname]

    def get_component(self, name, context=None):
        if type(context) == tuple:
            getcomponent = component.queryMultiAdapter
        else:
            getcomponent = component.queryAdapter
        if context is None:
            context = self.context
        self.cached_components[name] = getcomponent(context, name=name)
        return self.cached_components[name]

    def get_view(self, name):
        return self.get_component(name, (self.context, self.request))


class DisableBorderView(BaseView):
    """Disable border of the view"""

    def update(self):
        self.request.set('disable_border', 1)
        self.request.set('disable_plone.leftcolumn', 1)
        self.request.set('disable_plone.rightcolumn', 1)
