# Copyright (c) 2009 Infrae. All rights reserved.
# See also LICENSE.txt
# $Id$


from zope.interface import implements
from silva.core.views import views as silvaviews

from interfaces import IPageActions, IPageAction

class PageActions(silvaviews.ViewletManager):
    """See IPageActions
    """

    implements(IPageActions)


class PageAction(silvaviews.Viewlet):
    """See IPageAction
    """

    implements(IPageAction)

