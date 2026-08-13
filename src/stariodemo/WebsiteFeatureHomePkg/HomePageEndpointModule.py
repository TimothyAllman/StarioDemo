import uuid

from stario import Context
from stario import Writer
from stario import responses

from stariodemo.WebsiteFeatureChatAppPkg.GenerateColorModule import generate_color

from stariodemo.WebsiteFeatureChatAppPkg.GenerateUserNameModule import generate_username
from stariodemo.WebsiteFeatureHtmlComponentsPkg.PageHtmlModule import PageHtml
from stariodemo.WebsiteFeatureHomePkg.HomeHtmlModule import HomeHtml
from stariodemo.WebsiteFeatureCustomPkg.NavBarAndFooterHtmlModule import NavBarAndFooterHtml


def HomePageEndpoint():
    async def handler(c: Context, w: Writer) -> None:
        """
        Serve the home page
        """
        user_id = str(uuid.uuid4())[:8]
        username = generate_username()
        color = generate_color()

        # Pass empty collections - user will get real data after subscribing
        responses.html(
            w,
            PageHtml(
                NavBarAndFooterHtml(
                    HomeHtml(),
                )
            ),
        )

    return handler
