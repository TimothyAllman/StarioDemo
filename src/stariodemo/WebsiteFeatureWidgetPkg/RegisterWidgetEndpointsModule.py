from stario import App
from stario import Relay

from stariodemo.WebsiteFeatureWidgetPkg.HandleWidgetAddApiModule import WidgetAddEndpoint
from stariodemo.WebsiteFeatureWidgetPkg.HandleWidgetAddPageModule import WidgetAddPageEndpoint
from stariodemo.WebsiteFeatureWidgetPkg.HandleWidgetDetailsPageModule import WidgetDetailsPageEndpoint
from stariodemo.WebsiteFeatureWidgetPkg.HandleWidgetEditPageModule import WidgetEditPageEndpoint
from stariodemo.WebsiteFeatureWidgetPkg.UrlsWidgetModule import WIDGET_ADD_API_URL
from stariodemo.WebsiteFeatureWidgetPkg.UrlsWidgetModule import WIDGET_ADD_PAGE_URL
from stariodemo.WebsiteFeatureWidgetPkg.UrlsWidgetModule import WIDGET_DETAILS_PAGE_URL
from stariodemo.WebsiteFeatureWidgetPkg.UrlsWidgetModule import WIDGET_EDIT_PAGE_URL
from stariodemo.WebsiteFeatureWidgetPkg.UrlsWidgetModule import WIDGET_LIST_API_URL
from stariodemo.WebsiteFeatureWidgetPkg.UrlsWidgetModule import WIDGET_LIST_PAGE_URL
from stariodemo.WebsiteFeatureWidgetPkg.HandleWidgetListApiModule import WidgetListApiEndpoint
from stariodemo.WebsiteFeatureWidgetPkg.HandleWidgetListPageModule import WidgetListPageEndpoint


def WidgetRegisterEndpoints(app: App, relay: Relay):
    app.get(WIDGET_ADD_PAGE_URL, WidgetAddPageEndpoint())
    app.get(WIDGET_ADD_API_URL, WidgetAddEndpoint(relay))

    app.get(WIDGET_LIST_PAGE_URL, WidgetListPageEndpoint())
    app.get(WIDGET_LIST_API_URL, WidgetListApiEndpoint())

    app.get(WIDGET_EDIT_PAGE_URL, WidgetEditPageEndpoint())

    app.get(WIDGET_DETAILS_PAGE_URL, WidgetDetailsPageEndpoint())
