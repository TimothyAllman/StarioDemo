from stario import App

from stariodemo.WebsiteFeatureHomePkg.HomePageEndpointModule import HomePageEndpoint
from stariodemo.WebsiteFeatureHomePkg.HomeUrlsModule import HOME_PAGE_URL


def HomeRegisterEndpoints(app: App):
    app.get(HOME_PAGE_URL, HomePageEndpoint())
