from stario import Context
from stario import Writer

from stariodemo.DataStructsPkg.UserModule import UserDto
from stariodemo.HtmlComponentsPkg.PageModule import page
from stariodemo.HtmlViewsPkg.NavBarAndFooterViewModule import NavBarAndFooterView
from stariodemo.HtmlViewsPkg.XyzListViewModule import XyzListView
from stariodemo.HtmlViewsPkg.XyzSidebarViewModule import XyzSidebarView


def XyzListPageEndpoint(
    # Database: list[User],
):
    async def handler(c: Context, w: Writer) -> None:

        items = [
            UserDto(id="hfjjk9432024", username="bob", color="golden"),
            UserDto(id="823089whe0f", username="steve", color="blue"),
            UserDto(id="924900913", username="bella", color="red"),
            UserDto(id="hfjjk9432024", username="bob", color="golden"),
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
