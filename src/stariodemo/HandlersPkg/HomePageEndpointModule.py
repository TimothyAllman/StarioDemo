import uuid

from stario import Context, responses
from stario import Writer

from stariodemo.DataStructsPkg.GenerateColorModule import generate_color
from stariodemo.DataStructsPkg.GenerateUserNameModule import generate_username
from stariodemo.HtmlComponentsPkg.PageHtmlModule import PageHtml
from stariodemo.HtmlHtmlsPkg.HomeHtmlModule import HomeHtml
from stariodemo.HtmlHtmlsPkg.NavBarAndFooterHtmlModule import NavBarAndFooterHtml


def HomePageEndpoint():
    async def handler(c: Context, w: Writer) -> None:
        """
        Serve the home page
        """
        user_id = str(uuid.uuid4())[:8]
        username = generate_username()
        color = generate_color()

        # Pass empty collections - user will get real data after subscribing
        responses.html(w,
            PageHtml(
                NavBarAndFooterHtml(
                    HomeHtml(),
                )
            )
        )

    return handler
