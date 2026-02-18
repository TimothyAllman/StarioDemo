import time

from stario import asset
from stario import at
from stario import data
from stario.html import H1
from stario.html import Button
from stario.html import Div
from stario.html import Form
from stario.html import Head
from stario.html import Html
from stario.html import Input
from stario.html import Link
from stario.html import Meta
from stario.html import SafeString
from stario.html import Script
from stario.html import Span
from stario.html import Title
from stario.toys import toy_inspector

from stariodemo.DataStructsPkg.MessageModule import Message
from stariodemo.DataStructsPkg.UrlsModule import ABC_ADD_URL
from stariodemo.DataStructsPkg.UrlsModule import ABC_LIST_URL
from stariodemo.DataStructsPkg.UserModule import User
from stariodemo.HtmlComponentsPkg.FooterBarModule import FooterBar
from stariodemo.HtmlComponentsPkg.NavBarModule import NavBar
from stariodemo.HtmlComponentsPkg.PageModule import page
from stariodemo.HtmlComponentsPkg.SideBarButtonModule import SideBarButton
from stariodemo.HtmlComponentsPkg.SideBarModule import SideBar
from stariodemo.HtmlViewsPkg.InputFormViewModule import input_form_view
from stariodemo.HtmlViewsPkg.MessagesViewModule import messages_view
from stariodemo.HtmlViewsPkg.OnlineUsersViewModule import online_users_view
from stariodemo.HtmlViewsPkg.TypingIndicatorViewModule import typing_indicator_view


def LeftSidebarWithContentView(
    buttons,
    *children,
):
    """
    docstring
    """

    return Div(
        {"class": "grid grid-cols-1 lg:grid-cols-[200px_1fr]"},
        SideBar([item for item in buttons]),
        Div(
            {"class": "bg-red-500 w-full"},
            *children,
        ),
    )
