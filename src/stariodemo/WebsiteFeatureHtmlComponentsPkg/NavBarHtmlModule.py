from stario.markup.html import H1
from stario.markup.html import Div

from stariodemo.WebsiteFeatureAbcPkg.AbcUrlsModule import ABC_LIST_PAGE_URL
from stariodemo.WebsiteFeatureChatAppPkg.ChatAppUrlsModule import CHAT_PAGE_URL
from stariodemo.WebsiteFeatureGiveMePkg.GiveMeUrlsModule import PLOTLY_GRAPH_PAGE_URL
from stariodemo.WebsiteFeatureHomePkg.HomeUrlsModule import HOME_PAGE_URL
from stariodemo.WebsiteFeatureHtmlComponentsPkg.NavBarHtmlButtonModule import NavBarButtonHtml
from stariodemo.WebsiteFeatureWidgetPkg.WidgetUrlsModule import WIDGET_LIST_PAGE_URL


def NavBarHtml():
    return Div(
        {"class": "bg-backcolor1 p-4 flex items center"},
        Div(
            {"class": "flex items-center space-x-6 px-2"},
            H1(
                {"class": "text-frontcolor1 text-2xl font-bold"},
                "Stario With Tailwind",
            ),
        ),
        NavBarButtonHtml(name="Home", url=HOME_PAGE_URL.href()),
        NavBarButtonHtml(name="Abc", url=ABC_LIST_PAGE_URL.href()),
        NavBarButtonHtml(name="Widgets", url=WIDGET_LIST_PAGE_URL.href()),
        NavBarButtonHtml(name="Chat", url=CHAT_PAGE_URL.href()),
        NavBarButtonHtml(name="Graph", url=PLOTLY_GRAPH_PAGE_URL.href()),
    )
