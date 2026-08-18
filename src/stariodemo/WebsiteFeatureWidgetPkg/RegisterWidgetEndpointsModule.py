from stario import App
from stario import Relay

from stariodemo.WebsiteFeatureWidgetPkg.UrlsWidgetModule import WIDGET_ADD_API_URL
from stariodemo.WebsiteFeatureWidgetPkg.UrlsWidgetModule import WIDGET_ADD_PAGE_URL
from stariodemo.WebsiteFeatureWidgetPkg.UrlsWidgetModule import WIDGET_DETAILS_PAGE_URL
from stariodemo.WebsiteFeatureWidgetPkg.UrlsWidgetModule import WIDGET_EDIT_PAGE_URL
from stariodemo.WebsiteFeatureWidgetPkg.UrlsWidgetModule import WIDGET_LIST_API_URL
from stariodemo.WebsiteFeatureWidgetPkg.UrlsWidgetModule import WIDGET_LIST_PAGE_URL
from stariodemo.WebsiteFeatureWidgetPkg.HandleWidgetAddModule import WidgetAddEndpoint
from stariodemo.WebsiteFeatureWidgetPkg.WidgetAddPageEndpointModule import WidgetAddPageEndpoint
from stariodemo.WebsiteFeatureWidgetPkg.WidgetDetailsPageEndpointModule import WidgetDetailsPageEndpoint
from stariodemo.WebsiteFeatureWidgetPkg.WidgetEditPageEndpointModule import WidgetEditPageEndpoint
from stariodemo.WebsiteFeatureWidgetPkg.WidgetListApiEndpointModule import WidgetListApiEndpoint
from stariodemo.WebsiteFeatureWidgetPkg.WidgetListPageEndpointModule import WidgetListPageEndpoint


def WidgetRegisterEndpoints(app: App, relay: Relay):
    app.get(WIDGET_ADD_PAGE_URL, WidgetAddPageEndpoint())
    app.get(WIDGET_ADD_API_URL, WidgetAddEndpoint(relay))

    app.get(WIDGET_LIST_PAGE_URL, WidgetListPageEndpoint())
    app.get(WIDGET_LIST_API_URL, WidgetListApiEndpoint())

    app.get(WIDGET_EDIT_PAGE_URL, WidgetEditPageEndpoint())

    app.get(WIDGET_DETAILS_PAGE_URL, WidgetDetailsPageEndpoint())
