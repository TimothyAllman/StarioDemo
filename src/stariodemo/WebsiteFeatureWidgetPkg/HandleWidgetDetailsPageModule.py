from stario import Context
from stario import Writer
from stario import responses

from stariodemo.WebsiteFeatureCustomPkg.NavBarAndFooterHtmlModule import NavBarAndFooterHtml
from stariodemo.WebsiteFeatureHtmlComponentsPkg.PageHtmlModule import PageHtml

# Import the API route url object to resolve its href path at runtime
from stariodemo.WebsiteFeatureWidgetPkg.HtmlWidgetDetailsModule import WidgetDetailsHtml
from stariodemo.WebsiteFeatureWidgetPkg.HtmlWidgetSidebarModule import WidgetSideBarHtml


def WidgetDetailsPageEndpoint():
    async def handler(c: Context, w: Writer) -> None:
        """
        docstring
        """
        # 1. Extract the current raw ID path variable out of your route params dictionary
        widget_id = c.route.params.get("id", "").strip()

        # 3. CRITICAL FIXED: Added explicit "return" so the framework receives the payload
        return responses.html(
            w,
            PageHtml(
                NavBarAndFooterHtml(
                    WidgetSideBarHtml(
                        # 4. Pass the parameters directly into your updated layout signature
                        WidgetDetailsHtml(
                            widget_id=widget_id,
                        ),
                    )
                )
            ),
        )

    return handler
