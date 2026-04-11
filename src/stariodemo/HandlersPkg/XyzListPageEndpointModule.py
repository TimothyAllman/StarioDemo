from stario import Context
from stario import Writer

from stariodemo.DataStructsPkg.UserModule import User
from stariodemo.HtmlComponentsPkg.PageModule import page
from stariodemo.HtmlViewsPkg.NavBarAndFooterViewModule import NavBarAndFooterView
from stariodemo.HtmlViewsPkg.XyzListViewModule import XyzListView
from stariodemo.HtmlViewsPkg.XyzSidebarViewModule import XyzSidebarView


def XyzListPageEndpoint(
    # Database: list[User],
):
    async def handler(c: Context, w: Writer) -> None:

        items = [
            User(id="hfjjk9432024", username="bob", color="golden"),
            User(id="823089whe0f", username="steve", color="blue"),
            User(id="924900913", username="bella", color="red"),
            User(id="hfjjk9432024", username="bob", color="golden"),
        ]

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
