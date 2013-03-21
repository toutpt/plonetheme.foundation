from Acquisition import aq_inner, aq_parent
from zope import interface
from zope import schema
from plone.app.layout.viewlets.common import ViewletBase
from Products.CMFCore.utils import getToolByName
from plone.app.layout.navigation.interfaces import INavigationRoot
from collective.picturefill.interfaces import IPictureFill


class IOrbitContainer(interface.Interface):
    """Marker interface. Add this interface to a page where you want to
    display orbit"""


class OrbitOptionSchema(interface.Interface):
    """schema for orbit"""

    timer_speed = schema.Int(title=u"timer_speed", default=10000)
    animation_speed = schema.Int(title=u"", default=500)
    bullets = schema.Bool(title=u"", default=True)
    stack_on_small = schema.Bool(title=u"", default=True)


class OrbitViewlet(ViewletBase):
    """Make orbit usable as a slideshow
    """

    def update(self):
        super(OrbitViewlet, self).update()
        self.slides = []
        self.portal_catalog = getToolByName(self.context, 'portal_catalog')
        self.brains = self.get_items_brains()
        self.items = self.get_items_info()

    def options(self):
        return 'timer_speed:2500; bullets:false;'  # TODO: use configviews here

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
