from stario import Context
from stario import Writer
from stario import responses

from stariodemo.HtmlComponentsPkg.PageHtmlModule import PageHtml
from stariodemo.HtmlPkg.NavBarAndFooterHtmlModule import NavBarAndFooterHtml
from stariodemo.HtmlPkg.UserEditHtmlModule import UserEditHtml
from stariodemo.HtmlPkg.UserSidebarHtmlModule import UserSideBarHtml


def UserEditPageEndpoint():
    async def handler(c: Context, w: Writer) -> None:
        """
        Serve abc list page
        """
        responses.html(
            w,
            PageHtml(
                NavBarAndFooterHtml(
                    UserSideBarHtml(
                        UserEditHtml(),
                    )
                )
            ),
        )

    return handler
