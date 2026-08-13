from stario import App

from stariodemo.WebsiteFeatureGiveMePkg.GiveMeJsonEndpointModule import GiveMeJsonEndpoint
from stariodemo.WebsiteFeatureGiveMePkg.GiveMeTextEndpointModule import GiveMeTextEndpoint
from stariodemo.WebsiteFeatureGiveMePkg.GiveMeUrlsModule import GIVE_ME_JSON_URL
from stariodemo.WebsiteFeatureGiveMePkg.GiveMeUrlsModule import GIVE_ME_TEXT_URL
from stariodemo.WebsiteFeatureGiveMePkg.GiveMeUrlsModule import PLOTLY_GRAPH_PAGE_URL
from stariodemo.WebsiteFeatureGiveMePkg.PlotlyGraphPageEndpointModule import PlotlyGraphPageEndpoint


def GiveMeRegisterEndpoints(app: App):
    app.get(GIVE_ME_TEXT_URL, GiveMeTextEndpoint())
    app.get(GIVE_ME_JSON_URL, GiveMeJsonEndpoint())
    app.get(PLOTLY_GRAPH_PAGE_URL, PlotlyGraphPageEndpoint())
