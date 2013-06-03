from Products.CMFCore.utils import getToolByName
PROFILEID = 'profile-plonetheme.foundation:default'


def common(context):
    cleanup(context)
    setup = getToolByName(context, 'portal_setup')
    setup.runAllImportStepsFromProfile(PROFILEID)


def cleanup(context):
    setup = getToolByName(context, 'portal_setup')
    setup.runAllImportStepsFromProfile("profile-plonetheme.foundation:zclean")
