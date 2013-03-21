from plonetheme.sunburst.browser.interfaces import IThemeSpecific
from collective.z3cform.html5widgets.layer import Layer as BaseLayer


class Layer(IThemeSpecific, BaseLayer):
    """Browser layer"""


class DesktopLayer(Layer):
    """Specialized version for the plonetheme.foundationdesk"""
