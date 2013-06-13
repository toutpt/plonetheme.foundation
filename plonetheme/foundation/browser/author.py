from zope import interface
from plonetheme.foundation.browser import common
from zope.publisher.interfaces import IPublishTraverse


class IAuthorView(interface.Interface):
    """marker interface"""


@interface.implementer(IPublishTraverse)
class Author(common.DisableBorderView):
    interface.implements(IAuthorView)

    def __init__(self, context, request):
        super(Author, self).__init__(context, request)

        self.site_properties = None
        self.allowAnonymousViewAbout = None
        self.isAnon = None
        self.author = None
        self.mtool = None
        self.portal_url = None
        self.portal_state = None
        self.portrait = None
        self.authorinfo = None
        self.member = None

        if len(request.path) == 2:
            [self.author, self.viewname] = request.path
        elif len(self.request.path) == 1:
            self.author = request.path[0]
            self.viewname = 'author_view'

    def __call__(self):
        self.update()
        return self.index()

    def publishTraverse(self, request, name):
        """ used for traversal via publisher, i.e. when using as a url """
        self.author = name
        request['TraversalRequestNameStack'] = []
        # return self so the publisher calls this view
        return self

    def update(self):
        """
        portal_types context/portal_types;

        portal_url context/@@plone_portal_state/navigation_root_url;
        here_url context/@@plone_context_state/object_url;

        portal context/@@plone_portal_state/portal;
        email_from_address portal/email_from_address
        """
        super(Author, self).update()
        #dependencies
        if self.mtool is None:
            self.mtool = self.get_tool("portal_membership")
        if self.portal_state is None:
            self.portal_state = self.get_view("plone_portal_state")
        if self.portal_url is None:
            self.portal_url = self.get_tool("portal_url")
        if not self.site_properties:
            pp = self.get_tool('portal_properties')
            self.site_properties = pp.site_properties

        #info for the rendering
        if not self.allowAnonymousViewAbout:
            self.site_properties.getProperty('allowAnonymousViewAbout', True)
        if not self.isAnon:
            self.isAnon = self.portal_state.anonymous()
#        if not self.author:
#            traverse_subpath = self.request.get('traverse_subpath', '')
#            if len(traverse_subpath) > 0:
#                self.author = url_unquote_plus(traverse_subpath[0])
#            else:
#                self.author = self.request.get('author', None)
        if self.portrait is None and self.author:
            self.portrait = self.mtool.getPersonalPortrait(self.author)
        if self.authorinfo is None and self.author:
            self.authorinfo = self.mtool.getMemberInfo(self.author)
        if self.member is None:
            self.member = self.portal_state.member()
