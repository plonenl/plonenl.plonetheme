from zope.interface import implements, Interface

from Products.Five import BrowserView

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from AccessControl import getSecurityManager


class HomepageView(BrowserView):
    #implements(IMultiColumnView)

    template = ViewPageTemplateFile('templates/homepage.pt')