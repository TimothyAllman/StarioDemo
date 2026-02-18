import uuid

from stario import Context
from stario import Writer

from stariodemo.HtmlComponentsPkg.PageModule import page
from stariodemo.HtmlViewsPkg.NavBarAndFooterViewModule import NavBarAnfFooterView
from stariodemo.HtmlViewsPkg.XyzListViewModule import XyzListView
from stariodemo.HtmlViewsPkg.XyzSidebarViewModule import XyzSidebarView


def XyzListPageEndpoint(noDeps: None):
    async def handler(c: Context, w: Writer) -> None:

        # Pass empty collections - user will get real data after subscribing
        w.html(
            page(
                NavBarAnfFooterView(
                    XyzSidebarView(
                        XyzListView(),
                    )
                )
            )
        )

    return handler
