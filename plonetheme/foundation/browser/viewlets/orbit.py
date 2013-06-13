from Acquisition import aq_inner, aq_parent
from zope import interface
from zope import schema
from Products.CMFCore.utils import getToolByName
from plone.app.layout.navigation.interfaces import INavigationRoot
from collective.picturefill.interfaces import IPictureFill
from collective.configviews.browser.viewlet import ConfigViewlet


class IOrbitContainer(interface.Interface):
    """Marker interface. Add this interface to a page where you want to
    display orbit"""


class OrbitOptionSchema(interface.Interface):
    """schema for orbit"""

    timer_speed = schema.Int(title=u"timer_speed", default=10000)
    animation_speed = schema.Int(title=u"", default=500)
    bullets = schema.Bool(title=u"", default=True)
    stack_on_small = schema.Bool(title=u"", default=True)


class OrbitViewlet(ConfigViewlet):
    """Make orbit usable as a slideshow
    """
    settings_schema = OrbitOptionSchema

    def update(self):
        super(OrbitViewlet, self).update()
        self.slides = []
        self.portal_catalog = getToolByName(self.context, 'portal_catalog')
        self.brains = self.get_items_brains()
        self.items = self.get_items_info()

    def options(self):
        options = ""
        for key in self.settings:
            options += "%s:%s; " % (key, self.settings[key])
        return options

    def get_items_brains(self):
        context = aq_inner(self.context)
        if not INavigationRoot.providedBy(context):
            context = aq_parent(context)
        path = '/'.join(context.getPhysicalPath())
        query = {'portal_type': 'Image', 'Subject': 'Slideshow',
                 'path': path,
                 'sort_on': 'effective', 'sort_order': 'reverse'}
        brains = self.portal_catalog(**query)
        return brains

    def get_items_info(self):
        for brain in self.brains:
            self.slides.append({
                'title': brain.Title,
                'description': brain.Description,
                'picturefill': IPictureFill(brain)
            })
