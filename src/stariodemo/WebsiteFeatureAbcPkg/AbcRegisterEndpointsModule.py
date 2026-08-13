from stario import App

from stariodemo.WebsiteFeatureAbcPkg.AbcAddPageEndpointModule import AbcAddPageEndpoint
from stariodemo.WebsiteFeatureAbcPkg.AbcCalculationEndpointModule import AbcCalculationEndpoint
from stariodemo.WebsiteFeatureAbcPkg.AbcCalculationPageEndpointModule import AbcCalculationPageEndpoint
from stariodemo.WebsiteFeatureAbcPkg.AbcListPageEndpointModule import AbcListPageEndpoint
from stariodemo.WebsiteFeatureAbcPkg.AbcUrlsModule import ABC_ADD_PAGE_URL
from stariodemo.WebsiteFeatureAbcPkg.AbcUrlsModule import ABC_CALCULATION_PAGE_URL
from stariodemo.WebsiteFeatureAbcPkg.AbcUrlsModule import ABC_LIST_PAGE_URL
from stariodemo.WebsiteFeatureAbcPkg.AbcUrlsModule import API_ABC_CALCULATION_URL
from stariodemo.WebsiteFeatureAbcPkg.AbcUrlsModule import API_CALCULATION_URL
from stariodemo.WebsiteFeatureAbcPkg.ApiCalculationEndpointModule import ApiCalculationEndpoint


def AbcRegisterEndpoints(app: App):
    app.get(ABC_ADD_PAGE_URL, AbcAddPageEndpoint())
    app.get(ABC_LIST_PAGE_URL, AbcListPageEndpoint())
    app.get(ABC_CALCULATION_PAGE_URL, AbcCalculationPageEndpoint())
    app.get(API_CALCULATION_URL, ApiCalculationEndpoint())
    app.get(API_ABC_CALCULATION_URL, AbcCalculationEndpoint())
