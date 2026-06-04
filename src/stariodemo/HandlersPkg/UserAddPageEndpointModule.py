from stario import Context
from stario import Writer
from stario import responses

from stariodemo.HtmlComponentsPkg.PageHtmlModule import PageHtml
from stariodemo.HtmlHtmlsPkg.NavBarAndFooterHtmlModule import NavBarAndFooterHtml
from stariodemo.HtmlHtmlsPkg.UserAddHtmlModule import UserAddHtml
from stariodemo.HtmlHtmlsPkg.UserSidebarHtmlModule import UserSideBarHtml


def UserAddPageEndpoint():
    async def handler(c: Context, w: Writer) -> None:
        """
        Serve abc list page
        """
        responses.html(
            w,
            PageHtml(
                NavBarAndFooterHtml(
                    UserSideBarHtml(
                        UserAddHtml(),
                    )
                )
            ),
        )

    return handler
