import uuid

from stario import Context
from stario import Writer

from stariodemo.HtmlComponentsPkg.PageModule import page
from stariodemo.HtmlViewsPkg.NavBarAndFooterViewModule import NavBarAnfFooterView
from stariodemo.HtmlViewsPkg.XyzAddViewModule import XyzAddView
from stariodemo.HtmlViewsPkg.XyzSidebarViewModule import XyzSidebarView


def XyzAddPageEndpoint(noDeps: None):
    async def handler(c: Context, w: Writer) -> None:

        # Pass empty collections - user will get real data after subscribing
        w.html(
            page(
                NavBarAnfFooterView(
                    XyzSidebarView(
                        XyzAddView(),
                    )
                )
            )
        )

    return handler
