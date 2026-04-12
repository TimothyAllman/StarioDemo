from stario import Context
from stario import Writer

from stariodemo.HtmlComponentsPkg.PageModule import page
from stariodemo.HtmlViewsPkg.NavBarAndFooterViewModule import NavBarAndFooterView
from stariodemo.HtmlViewsPkg.XyzListViewModule import XyzListView
from stariodemo.HtmlViewsPkg.XyzSidebarViewModule import XyzSidebarView
from stariodemo.PiccoloPkg.GetWidgetsModule import GetWidgets


def XyzListPageEndpoint(
    # Database: list[User],
):
    async def handler(c: Context, w: Writer) -> None:

        items = await GetWidgets()

        # Pass empty collections - user will get real data after subscribing
        w.html(
            page(
                NavBarAndFooterView(
                    XyzSidebarView(
                        XyzListView(items),
                    )
                )
            )
        )

    return handler
