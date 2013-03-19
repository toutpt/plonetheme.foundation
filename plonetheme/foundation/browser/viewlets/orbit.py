from Acquisition import aq_inner, aq_parent
from zope import interface
from zope import schema
from plone.app.layout.viewlets.common import ViewletBase
from Products.CMFCore.utils import getToolByName


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
        parent = aq_parent(aq_inner(self.context))
        parent_path = '/'.join(parent.getPhysicalPath())
        query = {'portal_type': 'Image', 'Subject': 'Slideshow',
                 'path': parent_path,
                 'sort_on': 'effective', 'sort_order': 'reverse'}
        brains = self.portal_catalog(**query)

        for brain in brains:
            ob = brain.getObject()
            parent = ob.aq_parent
            self.slides.append({'title': parent.Title(),
                          'description': parent.Description(),
                          'imgtitle': ob.Title(),
                          'imgurl': ob.absolute_url(),
                          'url': parent.absolute_url()})

    def options(self):
        return ''  # TODO: use configviews here
