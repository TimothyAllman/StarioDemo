from stario.markup.html import H1
from stario.markup.html import Div

from stariodemo.DataStructsPkg.UrlsModule import ABC_LIST_PAGE_URL
from stariodemo.DataStructsPkg.UrlsModule import CHAT_PAGE_URL
from stariodemo.DataStructsPkg.UrlsModule import HOME_PAGE_URL
from stariodemo.DataStructsPkg.UrlsModule import USER_LIST_PAGE_URL
from stariodemo.HtmlComponentsPkg.NavBarHtmlButtonModule import NavBarButtonHtml


def NavBarHtml():
    return Div(
        {"class": "bg-blue-600 p-4 flex items center"},
        Div(
            {"class": "flex items-center space-x-6 px-2"},
            H1(
                {"class": "text-white text-2xl font-bold"},
                "Stario With Tailwind",
            ),
        ),
        NavBarButtonHtml(name="Home", url=HOME_PAGE_URL),
        NavBarButtonHtml(name="Abc", url=ABC_LIST_PAGE_URL),
        NavBarButtonHtml(name="Users", url=USER_LIST_PAGE_URL),
        NavBarButtonHtml(name="Chat", url=CHAT_PAGE_URL),
    )
